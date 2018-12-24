# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:56:06 2018

@author: bob
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

path = '../data/categories'
filename_list = os.listdir(path)

def plotEachFeature():
    for feature in [u'L', u'R', u'F', u'M', u'C']:
        plot_data = []
        for name in filename_list:
            filename = path + '/' + name
            data = pd.read_csv(filename)
            plot_data.append(data[feature].mean())
        print plot_data
        #for i in range(len(plot_data)):
        #    plot_data[i] = abs(plot_data[i])
        title = feature + '_class situation'
        plt.title(title)
        plt.bar([1,2,3,4,5], plot_data)
        plt.show()
    
#def plotEachClass():

for name in filename_list:
    filename = path + '/' + name
    data = pd.read_csv(filename)
    plot_data = data.mean(axis=0).values.tolist()
    #print plot_data
    print data.columns
    #for i in range(len(plot_data)):
    #    plot_data[i] = abs(plot_data[i])
    plt.title(name)
    plt.bar([1,2,3,4,5], plot_data)
    plt.show()