# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:48:21 2018

@author: atherll
"""


import pandas as pd
from pyramid.arima import auto_arima
from sklearn.preprocessing import LabelEncoder


df = pd.read_excel('timeseries.xlsx')
df.index = pd.DatetimeIndex(data = df['Date'], freq="d", start = 0, periods = 3321)
pd.to_datetime(df['Date'])
le = LabelEncoder()
df_e = df.apply(le.fit_transform)

train = df_e.loc['2009/06/02':'2017/12/31']
test = df_e.loc['2018/01/01':]

def a_arima(timeseries):
    
    stepwise_model = auto_arima(timeseries, start_p=1, start_q=1,
                               max_p=3, max_q=3, m=12,
                               start_P=0, seasonal=True,
                               d=1, D=1, trace=True,
                               error_action='ignore',  
                               suppress_warnings=True, 
                               stepwise=True)
    print(stepwise_model.aic())
    # Train the Model
    stepwise_model.fit(train)
    
    # Forecast
    future_forecast = stepwise_model.predict(n_periods=182)
    future_forecast
    future_forecast = pd.DataFrame(future_forecast, index = test.index, column=['Prediction'])
    pd.concat([test,future_forecast],axis=1).iplot()
    
a_arima(df_e['Onview Rate'])
