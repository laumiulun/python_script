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

def readfile_csv(filenameinput):
    out = np.loadtxt(open(filenameinput, "rb"), delimiter=",", dtype='str')
    return out
    numpy.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)

def basic_graph():
    while True:    
        filenameinput=raw_input("Enter file name: ")
        try:
            f = open(filenameinput)
            break
        except BaseException:
            print bcolors.RED+'ERROR: INPUT FILE NOT FOUND'+bcolors.N
        
    out = readfile_csv(filenameinput)
    title = out[0]
    for i in range(len(title)):
        title[i]=title[i].replace('"','')
    print title
    out = np.delete(out,[0],0)
    row=len(out)
    col=len(out[0])
    
    while True:
        numline = int(raw_input("How many dataline: "))        
        if isinstance(numline,(int,long)) == True:
            break
        else:
            print 'Error, not int'
    
    
    for i in range(numline):
        x = raw_input("What column is X: ")
        y = raw_input("What column is Y: ")
        
        xlabel=str(title[int(x)])
        ylabel=str(title[int(y)])
        
        xcol=[]
        for i in range(len(out)):
            xcol.append([])
            xcol[i]= float(out[i,int(x)])
        ycol=[]
        for i in range(len(out)):
            ycol.append([])
            ycol[i]= float(out[i,int(y)])
    
        plt.plot(xcol,ycol)
    plt.show()

