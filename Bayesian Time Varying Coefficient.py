# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 18:57:44 2018

@author: atherll
"""

import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt

df = pd.read_excel('timeseries.xlsx')

plt.plot(df['Date'],df['Dispatch Rate'])
plt.title('DR over Time')
plt.xlabel('Date')
plt.ylabel('Dispatch Rate')
plt.show()

df['DRlag'] = df['Dispatch Rate'].shift()
df.dropna(inplace=True)
with pm.Model() as model:
    sigma = pm.Exponential('sigma', 1./.02, testval=.1)
    nu = pm.Exponential('nu', 1./10)
    beta = pm.GaussianRandomWalk('beta',sigma**-2,shape=len(df['Dispatch Rate']))
    observed = pm.Normal('observed', mu=beta*df['DRlag'], sd = 1/nu, observed = df['Dispatch Rate'])
    
    trace = pm.sample()