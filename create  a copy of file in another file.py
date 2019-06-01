# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:43:48 2019

@author: Rai
"""


"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""


fp = open("word.txt","rt")
tp = open ('new.txt',mode='wt')
for line  in fp.readlines():
    print(line)
    tp.write(line+"\n") 
fp.close()
tp.close()