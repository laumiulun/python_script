import csv
import numpy as np
import os
import subprocess
from subprocess import call
from datetime import datetime
#def readfile(filenameinput):
#    with open(filenameinput) as f:
#        out=[]
#        for line in f:
#            line = line.split()
#            if line:
#                line=[str(i) for i in line]  # convert to str
#                out.append(line)
#    return out
def readfile2(filenameinput):
    with open(filenameinput, "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    lines = [line.rstrip('\n') for line in open(filenameinput)]
    return array

startTime = datetime.now()
########################################################
input_filename='temp_base.i'
output_filename='test_base.i'
# Read the file
raw_data=readfile2(input_filename)

xmax=14000 #nm
temp_array=range(1073,1683,10)
size_array=[1500]

outdata=raw_data

#####################################################
# for i in range(len(temp_array)):
for j in range(len(temp_array)):
    # Find particle size
    for i in range(len(raw_data)):
        if "[ICs]" in raw_data[i]:
            size_row=i
    
    outdata[size_row+4]='    radii = \''+str(size_array[0])+' '+str(size_array[0])+'\'\n'
    outdata[size_row+7]='    x_positions=\''+str(xmax/2-size_array[0])+' '+str(xmax/2+size_array[0])+'\'\n'
    # Change file name
    for i in range(len(raw_data)):
        if "file_base" in raw_data[i]:
            file_row=i
    
    outdata[file_row]='  file_base = ni_temp_'+str(temp_array[j])+'\n'
    
    # Change temperature 
    for i in range(len(raw_data)):
        if "[Materials]" in raw_data[i]:
            temp_row=i
    outdata[temp_row+4]='    T = '+str(temp_array[j])+' #K\n'
    
    with open(output_filename,'w') as the_file:
        for i in range(len(outdata)):
            the_file.write(outdata[i])
    
    subprocess.call('mpiexec -n 8 ../../marmot-opt -i '+output_filename,shell=True)
    
#######################################################
#with open(output_filename,'w') as the_file:
#    for i in range(len(outdata)):
#        the_file.write(outdata[i])
#



print datetime.now()-startTime