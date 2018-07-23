# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:11:55 2018

@author: atherll
"""
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

df = pd.read_excel('timeseries.xlsx')

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