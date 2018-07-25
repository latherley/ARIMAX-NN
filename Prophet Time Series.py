# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:03:30 2018

@author: atherll
"""

from fbprophet import Prophet 
import numpy as np
import pandas as pd

df = pd.read_excel('timeseries.xlsx')

df1 = pd.DataFrame(df(['Onview Rate','Date']))

df1['y'] = np.log(df['Onview Rate'])

df1['ds'] = df['Date']

model = Prophet(daily_seasonality = True) #instantiate Prophet
model.fit(df1) #fit the model with your dataframe

future_data = model.make_future_dataframe(periods=6, freq = 'm')

forecast_data = m.predict(future_data)