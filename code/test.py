# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:17:09 2018

@author: bob
"""
import numpy as np
import matplotlib.pyplot as plt

men_means = (20, 35, 30, 35, 27)

def PlotEach(data):
    ind = np.arange(5)  # the x locations for the groups
    width = 0.7  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, men_means, width, yerr=([1] * len(men_means)),
                    color='SkyBlue', label='Men')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind)
    ax.set_xticklabels(('C', 'R', 'F', 'M', 'L'))
    ax.legend()
    
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
    
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset['center'], 1.01*height,
                '{}'.format(height), va='bottom')
    plt.show()

PlotEach(men_means)
