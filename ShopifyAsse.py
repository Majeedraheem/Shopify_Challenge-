#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:19:41 2020

@author: mac
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:17:24 2020

@author: mac
"""
#import library 
import os
import pandas as pd
import numpy  as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats
from pandas import DataFrame
from pandas.plotting import scatter_matrix
#read the data set from the excel 
os.getcwd()
os.chdir('/Users/mac/Desktop')
df=pd.read_excel('Shopify.xlsx',index_col=0)
df.isnull().sum()
#Q:A: Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
#will use descrpitive analysis metric to understand key prefomance indicator average of (order_amount):
#to understand that we need prefomre descriptive analysis far its from data center which is the mean or the average
#Q:A Aswer:
# After Analysis the data 

#step one : 
metric=df.describe()
print(metric)

#step two:
##lets strat with viualization to check if the distrubiton is normal or not :

df.hist()
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.boxplot(df.order_amount)
# lets count number of  amounts and how many times that particular  amount occurs:
df_amountFreq = df
df_amountFreq['freq'] = df_amountFreq.groupby('order_amount')['order_amount'].transform('count')
frequency =df_amountFreq['freq'].value_counts(normalize =True)
print("Frequency of values as percentage in column 'order_amount' :")
print(frequency * 100)

df['order_amount'].quantile()
Q1=df_amountFreq['order_amount'].quantile(0.25)
Q3=df_amountFreq['order_amount'].quantile(0.75)
IQR= Q3-Q1

filtered = df_amountFreq.query('(@Q1 - 1.5 * @IQR) <= order_amount <= (@Q3 + 1.5 * @IQR)')
plt.boxplot(filtered.order_amount)
Avo=filtered['order_amount'].mean()
print(Avo)
outliers=len(df_amountFreq)-len(filtered)
print(outliers)

#ploting the diffrences between both data

#df.join(filtered, rsuffix='_filtered').boxplot()


filtered_2= filtered 
filtered_2['order_amount'].quantile()
Q1_2=filtered_2['order_amount'].quantile(0.25)
Q3_2=filtered_2['order_amount'].quantile(0.75)
IQR_2= Q3-Q1
filtered_2=filtered_2.query('(@Q1_2 - 1.5 * @IQR_2) <= order_amount <= (@Q3_2 + 1.5 * @IQR_2)')
plt.boxplot(filtered_2.order_amount)
Avo=filtered_2['order_amount'].mean()
print(Avo)
outliers_2=len(filtered)-len(filtered_2)
print(outliers_2)














