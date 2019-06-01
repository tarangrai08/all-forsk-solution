# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:13:53 2019

@author: Rai
"""


"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""


string = input("Enter day :").split()
string.insert(1,"tuesday")
string.insert(4,"friday")
string.insert(6,"sundayday")
print (string)


