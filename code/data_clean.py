# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 00:31:11 2018

@author: bob
"""

import pandas as pd

data_file = '../data/Original_data/air_data.csv'  #original data file
cleaned_data = '../data/Processed_data/data_cleaned.xls' #result cleaned data file

data = pd.read_csv(data_file, encoding='utf-8')
#remove the NaN value in data and return DataFrame
data[data['SUM_YR_1'].notnull() * data['SUM_YR_1'].notnull()]

index1 = data['SUM_YR_1'] != 0 #ticket's price isn't zero in first year
index2 = data['SUM_YR_2'] != 0 #ticket's price isn't zero in second year
index3 = (data['SEG_KM_SUM'] != 0) & (data['avg_discount'] != 0)
result = data[index1 | index2 | index3]

#result.to_excel(cleaned_data, index=False)