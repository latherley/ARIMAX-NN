# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:01:22 2018

@author: atherll
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# import data
df = pd.read_csv('timeseries.csv', parse_dates=True, index_col='Date')
print(df)

df[['Onview Rate','Dispatch Rate','Person Rate','Property Rate','Society Rate']].plot()
plt.show()

print(sm.tsa.statstools.adfuller(df['Onview Rate']))
print(sm.tsa.statstools.adfuller(df['Dispatch Rate']))
print(sm.tsa.statstools.adfuller(df['Person Rate']))
print(sm.tsa.statstools.adfuller(df['Property Rate']))
print(sm.tsa.statstools.adfuller(df['Society Rate']))