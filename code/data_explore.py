# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 01:00:46 2018

@author: bob
"""

import pandas as pd

#basci exploration on origin data
#find maximum and minimum in missing data and return the number

#the original data, index in the first row
data_file = '../data/Original_data/air_data.csv' 
#result of missing situation above
result_file = '../data/Processed_data/explore.csv' 


data = pd.read_csv(data_file, encoding='utf-8')
explore = data.describe(percentiles=[], include='all').T
#caculate the number of null by len(data) - 'count'
explore['null'] = len(data) - explore['count']
explore['null_per'] = explore['null'] / len(data)
explore = explore[['null', 'null_per', 'max', 'min']]
explore.to_csv(result_file)