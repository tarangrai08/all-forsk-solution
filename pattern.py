# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:44:09 2019

@author: Rai
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""


num=int(input("enter no of element"))
for i in range(1,num+1):
    print ("*"*i)
for i in range(num-1,0,-1):
    print ("*"*i)

