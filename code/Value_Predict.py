# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 04:10:09 2018

@author: bob
"""
#import py files
import Clientdata
import Kmeans
import K_means_cluster

#run model:
input_file = '../data/Processed_data/model_input.csv'   #get model_input 
K_means_model, centers, labels = Kmeans.kmeans()

#display the detiles of the Cluster
print "Details of Cluster"
K_means_cluster.resultOfCluster(centers, labels)
print "Every Attr Feature"
K_means_cluster.plotEveryFeature(labels)
print "Every Value Distribution"
K_means_cluster.labelPlot(labels, 5, centers)

#get prepared for predicting the Value of Client 
input_data = Clientdata.Get_input_data()

#Predict
client_laber = K_means_model.predict(input_data)
print "This Client's Value is {}\n".format(client_laber)
