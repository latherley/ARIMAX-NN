# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:48:27 2018

@author: atherll
"""

import pandas as pd
df = pd.read_excel('timeseries.xlsx')
df.index = pd.to_datetime(df['Date'])
df['Person Rate'].plot()

import statsmodels.api as sm
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df['Person Rate'],lags = 16, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df['Person Rate'], lags = 16, ax=ax2)
plt.show()

from statsmodels.tsa.stattools import adfuller as adf
x = df['Call Rate']
result = adf(x)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')

model=sm.tsa.ARIMA(endog=df['Call Rate'],order=(0,1,6))
results=model.fit(start_params=)
print(results.summary())

def test_stationarity(timeseries):
    
    #Determing Rolling Statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)
    
    #plot rolling statistics
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
    print ('dfoutput')
                    
test_stationarity(df['Person Rate'])        
pd.Panel.update
pd.__version__