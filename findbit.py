#!/usr/bin/env python2
# -*- coding: utf-8 -*-

filename = 'solidifcations.tex'
while True:
    #filenameinput=raw_input("Enter file name: ")
    try:
        f = open(filenameinput)
        break
    except BaseException:
        print 'ERROR: INPUT FILE NOT FOUND'

bit = str(raw_input("Bitinput:"))
with open(filenameinput) as fp:
    for i, line in enumerate(fp):
        if bit in line:
            print i, repr(line)
