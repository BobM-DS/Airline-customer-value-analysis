# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 05:19:38 2018

@author: bob
"""

import pandas as pd

data_file = '../data/Processed_data/standardization.csv'
data_output = '../data/Processed_data/model_input.csv'
data_statics = '../data/Processed_data/data_statics.csv'
data_mean_path = '../data/Processed_data/data_mean.csv'
data_std_path = '../data/Processed_data/data_std.csv'

#get input DataFrame
data = pd.read_csv(data_file)

#standardization procedure
data = (data - data.mean(axis=0)) / (data.std(axis=0))
data_mean = data.mean(axis=0)
data_std = data.std(axis=0)
data_mean.to_csv(data_mean_path)
data_std.to_csv(data_std_path)

data.columns = ['Z'+i for i in data.columns] #columns rename
#data_record.to_csv(data_statics)
data.to_csv(data_output, index=False)
