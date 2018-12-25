# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 03:36:51 2018

@author: bob
"""
import matplotlib.pyplot as plt
import numpy as np

def PlotCluster(data, laber):
    data = [round(i, 2) for i in data]
    
    ind = np.arange(5)  # the x locations for the groups
    width = 0.7  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, data, width, yerr=(np.std(data)),
                    color='SkyBlue')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    title = 'Cluster' + '_' + str(laber)
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(('Avg_C', 'Recent', 'Frequrent', 'Miles', 'Length'))
    ax.legend()
    
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
    
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset['center'], 1.01*height,
                '{}'.format(height), va='bottom')
    fig_path_name = '../data/result/' + str(laber)
    plt.savefig(fig_path_name)
    plt.show()