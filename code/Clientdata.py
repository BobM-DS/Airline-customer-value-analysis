# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 04:26:26 2018

@author: bob
"""
import numpy as np
import pandas as pd
#get data prepared

#get dataset's mean and std return both
def Get_Mean_Std():
    data_mean_path = '../data/Processed_data/data_mean.csv'
    data_std_path = '../data/Processed_data/data_std.csv'
    mean = pd.read_csv(data_mean_path, names=['attr', 'mean']).T.ix['mean'].values
    std = pd.read_csv(data_std_path, names=['attr', 'std']).T.ix['std'].values
    return mean, std

def Get_input_data():
    print "Please input the Client's data"
    Load_time = input("Load_time(0~200): ")
    Last_to_end = input("Last_to_end(0~1000): ")
    Flight_count = input("Flight_count(0~300): ")
    Seg_km_sum = input("Seg_km_sum(0~600000): ")
    Avg_discount = input("Avg_discount(0~1.5): ")
    
    mean, std = Get_Mean_Std()
    input_data = np.array([Load_time, Last_to_end, Flight_count, \
                                Seg_km_sum, Avg_discount])
    model_input = (input_data-mean) / (std)
    return model_input
