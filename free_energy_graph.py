#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:29:25 2018

@author: andy
"""
import math as math
import numpy as np
import matplotlib.pyplot as plt

def freefunction(inputlist,X):
    gc=[]
    for i in range(len(X)):
        gc.append(0)
        gc[i]=inputlist[0]*X[i]
        +inputlist[1]*(1-X[i])
        +inputlist[2]*X[i]*np.log(X[i])
        +inputlist[3]*(1-X[i])*np.log((1-X[i]))
        +inputlist[4]*X[i]*(1-X[i])
        +inputlist[5]*X[i]*(1-X[i])*((2*X[i])-1)
        +inputlist[6]*X[i]*(1-X[i])*((2*X[i])-1)*((2*X[i])-1)
    return gc
f=[-24468.1,-28275.33,4167.994,7052.907,12089.93,2568.625,-2345.293]

#f2=[-32.770969,-25.8186669,-3.29612744,17.669757,37.5197853,20.6941796,10.8095813]

X=np.linspace(0,1.0, num=150)

Fc=freefunction(f,X)

plt.plot(X,Fc)