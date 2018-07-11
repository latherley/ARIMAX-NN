# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:53:34 2018

@author: atherll
"""
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

series = pd.read_excel('timeseries.xlsx', header=0, parse_dates=[0], index_col=0, squeeze=True)

# fit model
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())


np.asarray(series)