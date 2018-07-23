# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:03:30 2018

@author: atherll
"""

from fbprophet import Prophet 
import numpy as np
import pandas as pd

df = pd.read_excel('timeseries.xlsx')

df['Onview Rate Orig'] = df['Onview Rate'] # to save a copy of the original data..you'll see why shortly. 
# log-transform y
df['Onview Rate'] = np.log(df['Onview Rate'])

df['y'] = df['Onview Rate']
df['ds'] = df['Date']

model = Prophet() #instantiate Prophet
model.fit(df); #fit the model with your dataframe

future_data = model.make_future_dataframe(periods=190)

forecast_data = predict(future_data)