# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:03:30 2018

@author: atherll
"""

from fbprophet import Prophet 
import numpy as np
import pandas as pd

df = pd.read_excel('timeseries.xlsx')
