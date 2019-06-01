# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:16:21 2019

@author: Rai
"""


"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

import csv
with open ("zoo.csv","r") as csv.file:
      csv_reader = csv.reader(csv.file, delimiter=",")
      next(csv_reader)
      for row in csv_reader:
        print (row) 
        
list1 = []    
import csv
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        print ( row[0] )    
        
    
       
import csv
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        
        print ( row[2] )        
        count +1= count
        
        
        
        
        
        
        