# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:43:28 2018

@author: atherll
"""

import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

df = pd.read_excel('timeseries.xlsx', index_column = 'Date')
df.set_index('Date')

def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()

    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
    
test_stationarity(df['Dispatch Rate'])  
test_stationarity(df['Onview Rate'])


def auto_partial_autocorrelation(timeseries):

    fig = plt.figure(figsize=(12,8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(timeseries, lags = 40, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(timeseries, lags = 40, ax=ax2)
    ax1.set_title('Crime Rate - Autocorrelation')
    ax2.set_title('Crime Rate - Partial Autocorrelation')
    plt.show()
    
    
auto_partial_autocorrelation(df['Onview Rate'])

import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def decompose(timeseries):
    
    ts_log = np.log(timeseries)
    decomposition = seasonal_decompose(ts_log)
    
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    
    plt.subplot(411)
    plt.plot(ts_log, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal,label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()
    
decompose(df['Dispatch Rate'])

def difference(timeseries):

    ts_log_diff = np.log(timeseries) - np.log(timeseries).shift()
    plt.plot(ts_log_diff)

    ts_log_diff.dropna(inplace=True)

difference(df['Crime Rate'])

import cufflinks as cf
from pyramid import auto_arima



def a_arima(timeseries):
    
    stepwise_model = auto_arima(timeseries, start_p=1, start_q=1,
                               max_p=3, max_q=3, m=12,
                               start_P=0, seasonal=True,
                               d=1, D=1, trace=True,
                               error_action='ignore',  
                               suppress_warnings=True, 
                               stepwise=True)
    #print(stepwise_model.aic())

    #df['Year'] = pd.to_datetime(df['Year'])
    train = df.loc['2009-06-02 00:00:00':'2017-12-31 00:00:00']
    test = df.loc['2018-01-01 00:00:00':]
    
    # Train the Model
    stepwise_model.fit(train)

    future_forecast = stepwise_model.predict(n_periods=182)
    future_forecast = pd.DataFrame(future_forecast, index = test.index, column=['Prediction'])
    pd.concat([test,future_forecast],axis=1).iplot()

a_arima(df['Onview Rate'])