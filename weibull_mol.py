#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:38:42 2018

@author: andy
"""
# The goal of this script is to test the signifcant of the
# weibull mol in  

import numpy as np
import matplotlib.pyplot as plt


mol=np.arange(1,31)


n=[]
for i in range(len(mol)):
    n[i]=[(np.log(1))/np.log(0.5)]^(1/mol[i])
    