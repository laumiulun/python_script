# -*- coding: utf-8 -*-
#!/usr/bin/env python 
"""
Created on Fri Mar 02 11:28:13 2018

@author: Andy Lau
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

# COLORS CLASS
class bcolors:
    N='\033[0m'             #Normal
    BOLD = '\033[1m'        #Bold
    UNDERL = '\033[4m'      #Underline
    RED = '\033[91m'        #RED
    GREEN = '\033[42m'      #GREEN

def readfile(filenameinput):
    with open(filenameinput) as f:
        out=[]
        for line in f:
            line = line.split(',')
            if line:
                line=[str(i) for i in line]  # convert to str
                out.append(line)
    return out

def readfile2(filenameinput):
    out = np.loadtxt(open(filenameinput, "rb"), delimiter=",", dtype='str')
    return out
    numpy.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)

def Tryfile(command,message):
    try:
        f= open(command)
    except BaseException:
        print bcolors.RED+'ERROR: ' +str(message) +' NOT FOUND'+bcolors.N
        sys.exit() 


#################

filenameinput=raw_input("Enter file name: ")
Tryfile(filenameinput,'Inputfile')
#filenameinput = 'Onecrack0.csv'

#out=readfile(filenameinput)

out = readfile2(filenameinput)
title = out[0]
out = np.delete(out,[0],0)

row=len(out)
col=len(out[0])





#title = out[0]
#time = float(out)




#for i in range(len(out)):
#    x1.append([])
#    x2.append([])
#    x1[i]=float(out[i][0])
#    x2[i]=float(out[i][5])
#    
#
#
#plt.plot(x2,x1,'r-')
#
#plt.xlabel('Radius(m)')
#plt.ylabel('Temperature(K)')
#'''plt.ylabel('Thermal Conductivity($W/m^{2}*K$)')'''
#
#plt.show()
