# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:20:24 2019

@author: Rai
"""


"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
list1 = []
tp = open ("absentee.txt","wt")
for i in range(0,26):
    inp = input("enter the name of student: ")
    if not inp :
        break
    list1.append(inp)    
    print (list1)