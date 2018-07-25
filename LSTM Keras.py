# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:26:52 2018

@author: atherll
"""

from pandas import read_csv
from matplotlib import pyplot

# load dataset
dataset = pd.read_excel('timeseries.xlsx')
values = dataset.values

# specify columns to plot
groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
# plot each column
pyplot.figure()
for group in groups:
	pyplot.subplot(len(groups), 1, i)
	pyplot.plot(values[:, group])
	pyplot.title(dataset.columns[group], y=0.5, loc='right')
	i += 1
pyplot.show()