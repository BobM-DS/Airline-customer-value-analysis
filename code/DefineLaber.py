#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:24:28 2018

@author: bob
"""

def Relaber(predict_laber):
    predict = int(predict_laber)
    if predict == 0:
        laber = 'Important retention customer'
    if predict == 1:
        laber = 'Valuable customer'
    if predict == 2:
        laber = 'Worth developing'
    if predict == 3:
        laber = 'Normal'
    if predict == 4:
        laber = 'Low valuable'
    return laber