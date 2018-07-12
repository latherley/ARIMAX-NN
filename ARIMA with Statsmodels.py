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
fig = sm.graphics.tsa.plot_acf(df['Person Rate'],lags = 40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df['Person Rate'], lags = 40, ax=ax2)
plt.show()

print(sm.tsa.stattools.adfuller('Person Rate', maxlag=None)