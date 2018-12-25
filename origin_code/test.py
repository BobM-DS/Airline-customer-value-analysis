#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:11:25 2018

@author: bob
"""

#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

inputfile = '../data/temp/zscoreddata.xls' 
k = 5                    


data = pd.read_excel(inputfile) #


kmodel = KMeans(n_clusters = k, n_jobs = 4) #
kmodel.fit(data) #

kmodel.cluster_centers_
kmodel.labels_ 
x = [1.0989423842,-0.9008699207,3.1202488347,3.8241744646,-0.2289724862]
x_new = np.array(x).reshape(1, -1)

pre = kmodel.predict(x_new)
print pre