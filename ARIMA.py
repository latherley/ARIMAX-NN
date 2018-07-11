# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:53:34 2018

@author: atherll
"""
import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt

df = pd.read_excel('timeseries.xlsx')

plt.plot(df['Date'],df['Person Rate'])
plt.title('Crime Over Time')
plt.xlabel('Date')
plt.ylabel('Person Rate')
plt.show()

df['lag'] = df['Person Rate'].shift()
df.dropna(inplace=True)
with pm.Model() as model:
    sigma = pm.Exponential('sigma', 1./.02, testval=.1)
    nu = pm.Exponential('nu', 1./10)
    beta = pm.GaussianRandomWalk('beta',sigma**-2,shape=len(df['Person Rate']))
    observed = pm.Normal('observed', mu=beta*df['lag'], sd = 1/nu, observed = df['Person Rate'])
    
    trace = pm.sample()
    
plt.plot(df.index,trace['beta'].T, 'b', alpha=.03)
plt.title('Person Rate Growth Rate')
plt.xlabel('Date')
plt.ylabel('Growth Rate')
plt.show()