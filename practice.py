# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:39:38 2020

@author: sjrsn
"""

#Topic ---- Case Study - Denco - Manufacturing Firm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%case details
#%%Objective
#Expand Business by encouraging loyal customers to Improve repeated sales
#Maximise revenue from high value parts
#%%Information Required
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#%%%
#see all columns
pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
ug=pd.read_csv('denco.csv')
ug
ug1= ug.groupby('custname').count().sort_values(by='region',ascending=0) 
ug1.iloc[0:5,0:1].plot(kind='bar')  #high volume
ug.groupby('custname').count().sort_values(by='region',ascending=1).iloc[0:5,0:1].plot(kind='bar')#low volume
ug.groupby('custname').sum().sort_values(by='revenue',ascending=0).iloc[0:5,1].plot(kind='bar')#high revenue 
ug.groupby('partnum').sum().sort_values(by='margin',ascending=0).iloc[0:5,2].plot(kind='bar')#high margin
ug.groupby("region").count().sort_values(by='region',ascending=1).iloc[0:5,0].plot(kind='bar')
#ug.groupby('partnum').sum().sort_values(by= ['margin','revenue'],ascending=0)
groupby ?
