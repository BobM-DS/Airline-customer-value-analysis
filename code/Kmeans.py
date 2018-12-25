# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 04:34:44 2018

@author: bob
"""

import pandas as pd
from sklearn.cluster import KMeans

#run Kmeans model
#return model ,centers of each clusters and labels of the datasets
def kmeans():
    input_file = '../data/Processed_data/model_input.csv'
    
    k = 5 # set the number of clustering
    
    data = pd.read_csv(input_file)
    
    k_model = KMeans(n_clusters=k, n_jobs=7) 
    k_model.fit(data)
    
    centers = k_model.cluster_centers_ #centery of clustering
    labels = k_model.labels_ #labels
    return k_model, centers, labels