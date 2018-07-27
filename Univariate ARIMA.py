# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:29:55 2018

@author: atherll
"""

import pandas as pd
from pandas import datetime
from matplotlib import pyplot
from sklearn.preprocessing import LabelEncoder
from pandas.tools.plotting import autocorrelation_plot

df = pd.read_excel('timeseries.xlsx')
df.index = pd.DatetimeIndex(data = df['Date'], freq="d", start = 0, periods = 3321)
pd.to_datetime(df['Date'])


