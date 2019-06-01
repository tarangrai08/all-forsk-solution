# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:18:10 2019

@author: Rai
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def fix_teen(n):
    lst=[13,14,17,18,19]
    if n in lst:
        return 0
    else:
        return n
user_inp = input('enter the keys:')
user_inp = user_inp.split(',')
dict1={}
for inp in user_inp:
    inp=inp.split(':')
    inp[0]=inp[0].replace('"','')
    dict1[inp[0]]=int(inp[1])
sum1=0
for key,value in dict1.items():
    val=fix_teen(value)
    sum1+=val
print(sum1)

