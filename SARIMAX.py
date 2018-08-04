# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:42:55 2018

@author: atherll
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import *
import sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm  
from statsmodels.tsa.stattools import acf  
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

#read data frome excel
df = pd.read_excel('timeseries.xlsx')
df.index = pd.DatetimeIndex(df['Date'], freq="d", start = 1, periods = 3321)



#plot raw counts
df['total crime'].plot(legend=True, color = 'red');
df['Onview'].plot(legend=True, figsize=(30,8), secondary_y=True,
                      title='All Crime and Proactive Behavior', color = 'blue')
plt.show()
  
#plot rate to control for population growth
df['Crime Rate'].plot(legend=True, color = 'red');
df['Onview Rate'].plot(legend=True, figsize=(30,8), secondary_y=True,
                      title='All Crime and Proactive Behavior', color = 'blue')
plt.show()

#plot the components
df['Person Rate'].plot(legend=True, color = 'red');
df['Property Rate'].plot(legend=True, color = 'green');
df['Society Rate'].plot(legend=True, color = 'yellow');
df['Onview Rate'].plot(legend=True, figsize=(30,8), secondary_y=True,
                      title='All Crime and Proactive Behavior', color = 'blue')
plt.show()

#Decompose the series
def decompose(timeseries,column):
    decomposition = seasonal_decompose(timeseries[column], freq=12)  
    fig = plt.figure()  
    fig = decomposition.plot()  
    plt.title(column)
    fig.set_size_inches(30, 8)
    plt.show()   

decompose(df,'Person Rate')
decompose(df,'Property Rate')
decompose(df,'Society Rate')
decompose(df,'Onview Rate')


def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(window=12,center=False).mean();
    rolstd = timeseries.rolling(window=12,center=False).std();

    #Plot rolling statistics:
    fig = plt.figure(figsize=(15, 5))
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

test_stationarity(df['Person Rate'])
test_stationarity(df['Property Rate'])
test_stationarity(df['Society Rate'])
test_stationarity(df['Onview Rate'])

# Log is a minor improvement, meaning that the variance is stable
def log(timeseries):
    log = timeseries.apply(lambda x: np.log(x))  
    test_stationarity(log)
    test_stationarity(timeseries)
    
log(df['Person Rate'])
log(df['Property Rate'])
log(df['Society Rate'])
log(df['Onview Rate'])

def diff1(timeseries):
    diff1 = timeseries - timeseries.shift(1)  
    test_stationarity(diff1.dropna(inplace=False)) 
    test_stationarity(timeseries)

diff1(df['Person Rate'])
diff1(df['Property Rate'])
diff1(df['Society Rate'])
diff1(df['Onview Rate'])

    #-6.608968e+00
# Seasonal difference: take a weekly season improves stationarity even more
air['visit_mean_seasonal'] = air.visit_mean - air.visit_mean.shift(7)
test_stationarity(air.visit_mean_seasonal.dropna(inplace=False)) #-7.196314e+00
# Seasonal and 1st difference is even better, but we were already well within the 1% confidence interval
air['visit_mean_seasonal_diff'] = air.visit_mean_diff - air.visit_mean_diff.shift(7)
test_stationarity(air.visit_mean_seasonal_diff.dropna(inplace=False)) #-9.427797e+00