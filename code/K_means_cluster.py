# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 05:34:39 2018

@author: bob
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import csv

input_file = '../data/Processed_data/model_input.csv'

k = 5 # set the number of clustering

data = pd.read_csv(input_file)

k_model = KMeans(n_clusters=k, n_jobs=1)
k_model.fit(data)

centers = k_model.cluster_centers_ #centery of clustering
labels = k_model.labels_ #labels

#create a table that describe the result of cluster
def resultOfCluster(center, labels):  
    whole_info = []
    clu_class = list(set(labels))
    for i in range(0, 5):
        row = []
        row.append(clu_class[i])
        row.append(labels.tolist().count(i))
        for j in range(0, 5):
            row.append(center[i][j])
        whole_info.append(row)
    
    result_of_cluster = pd.DataFrame(np.array(whole_info), 
                      columns=['cluster_class',
                               'cluster_number',
                               'ZL',
                               'ZR',
                               'ZF',
                               'ZM',
                               'ZC'])
    print result_of_cluster
    #save file
    #result_of_cluster.to_excel('../data/Processed_data/ResultOfCluster.xls', index=False)
    return result_of_cluster

#resultOfCluster(centers, labels)

#return a dic contains all classes' values
def resultOfClass(labels):
    class_dic = {}
    for i in range(0, len(set(labels))):
        class_dic[str(i)] = []
    index_arr = range(0, len(data))
    for index, label in zip(index_arr, labels):
        row = data.ix[index].values
        class_dic[str(label)].append(row)
    return class_dic

#plot the each feature's situation
def plotEveryFeature(class_dic):
    for feature in range(0, 5):# C, R, F, M, L
        plot_arr = []
        for class_number in range(0, 5): #for every Class 
            arr = np.array(class_dic[str(class_number)])
            plot_arr.append(arr[:,feature].mean())
        plt.bar([1,2,3,4,5], plot_arr)
        plt.show()

class_dic = resultOfClass(labels)

for cate in class_dic.keys():
    cate_info = class_dic[cate]
    cate_arr = np.array(cate_info)
    filepath = '../data/categaries/'
    filename = 'category_' + cate
    target = filepath + filename + '.csv'
    with open(target, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['L', 'R', 'F', 'M', 'C'])
        writer.writerows(cate_info)
    print "Category is: ", cate, 
    print "Mean is: ", cate_arr.mean(axis=0)