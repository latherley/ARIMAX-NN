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

df = pd.read_excel('timeseries.xlsx')

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