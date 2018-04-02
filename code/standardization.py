# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 05:19:38 2018

@author: bob
"""

import pandas as pd

data_file = '../data/Processed_data/standardization.csv'
data_output = '../data/Processed_data/model_input.csv'

#get input DataFrame
data = pd.read_csv(data_file)

#standardization procedure
data = (data - data.mean(axis=0)) / (data.std(axis=0))
data.columns = ['Z'+i for i in data.columns] #columns rename

data.to_csv(data_output, index=False)