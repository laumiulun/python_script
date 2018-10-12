#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:37:44 2018

@author: andylau
"""

import sys,glob,os
#
#fnames = listdir('.')
#
#
#print len(fnames)
#base_file = raw_input("File_base input: ")

#Driver 
if len(sys.argv) != 3:
    print "Useage: <program name> <input_dir> <out_name>"
    sys.exit(1)
else:
    temp = sys.argv[1]

#fnames = listdir('.')

inputglob = os.path.join(sys.argv[1],'*png')
index = 0
for infile in sorted(glob.glob(inputglob)):
    print "Current File Being Processed is: " + infile
    print "Output File is: "sys.argv[2]+str(index)+".png"
    os.rename(infile,sys.argv[2]+str(index)+".png")
    index+=1

print END