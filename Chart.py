import matplotlib.pyplot as plt
import numpy as np
import math


def pchart(array,numofobersvations):
    
    totaldefectives=float(sum(array))
    totalobserv=len(array)*numofobservations
    fractdefect=[x/numofobservations for x in array]
    x=range(len(array))

    paverage=sum(array)/totalobserv

    ucl=paverage+3*(math.sqrt((paverage*(1-paverage))/numofobservations))
    lcl=paverage-3*(math.sqrt((paverage*(1-paverage))/numofobservations))

    if lcl < 0.0:
	    lcl = 0.0


    plt.plot(x,fractdefect)
    plt.axhline(y=paverage,color='black')
    plt.axhline(y=ucl,ls='dashed',color='r')
    plt.axhline(y=lcl,ls='dashed',color='r')

    plt.show()

def cchart(array,Title):
    
    numofcomp=float(sum(array))
    number=float(len(array))
    cavg=numofcomp/number

    
    ucl=cavg+3*math.sqrt(cavg)
    lcl=cavg-3*math.sqrt(cavg)
    print lcl
    if lcl < 0:
        lcl=0
        
    x=range(len(array))

    print "STAT"
    print "CAVG: ", cavg
    print "UCL: ", ucl
    print "LCL: ", lcl
    
    plt.plot(x,array,'o--')
    plt.axhline(y=cavg,color='black')
    plt.axhline(y=ucl,ls='dashed',color='r')
    plt.axhline(y=lcl,ls='dashed',color='r')

    plt.title(Title)
    plt.show()

def cpk(USL,LSL,mu,sigma):

    firstvalue=((float(USL)-mu)/(3*sigma))
    secondvalue=((float(mu)-LSL)/(3*sigma))
    return min(firstvalue,secondvalue)
    
def cp(USL,LSL,sigma):

    return (float(USL)-LSL)/(6*sigma)    




print cpk(100,70,80,5)
print cp(100,70,5)
array=[1, 2, 4, 0.7, 0.5, 05]

cchart(array,'random_data')
