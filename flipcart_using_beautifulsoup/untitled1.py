#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:03:18 2021

@author: sangeeth
"""

import csv

data = [['Geeks'], [4], ['geeks !']] 
  
# opening the csv file in 'w+' mode 
file = open('g4g.csv', 'w+', newline ='') 
  
# writing the data into the file 
with file:     
    write = csv.writer(file) 
    write.writerows(data) 