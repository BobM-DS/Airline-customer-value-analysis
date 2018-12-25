# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 02:04:48 2018

@author: bob
"""
import pandas as pd
import datetime
import csv

data_file = '../data/Processed_data/data_cleaned.xls'
data_output = '../data/Processed_data/standardization.csv'

data = pd.read_excel(data_file, 
                     usecols=['FFP_DATE', 'LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount',
                               'SEG_KM_SUM', 'LAST_TO_END'])

def change2datetime(time):
    time = time.split('/')
    time = [int(i) for i in time]
    return time

def month_differ(x, y):
    month_differ = abs((x.year - y.year) * 12 + (x.month - y.month) * 1)
    return month_differ    

#def month_number(data):
result = []
for index, row in data.iterrows():
    f = str(row['FFP_DATE'])
    l = str(row['LOAD_TIME'])
    ffp = change2datetime(f)
    load = change2datetime(l)
    ffp_month = datetime.datetime(ffp[0], ffp[1], ffp[2])
    load_month = datetime.datetime(load[0], load[1], load[2])
    
    L = month_differ(load_month, ffp_month)
    R = row['LAST_TO_END']
    F = row['FLIGHT_COUNT']
    M = row['SEG_KM_SUM']
    C = row['avg_discount']
    target = [L, R, F, M, C]
    result.append(target)
    #mon.append(month)
#return mon

#write to csv 
'''
with open(data_output, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['L', 'R', 'F', 'M', 'C'])
    writer.writerows(result)
'''


    
    
