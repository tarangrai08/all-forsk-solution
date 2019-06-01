# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:38:25 2019

@author: Rai
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""


import pandas as pd
df = pd.read_csv("Automobile.csv")
df = df.fillna(round(df.mean(),0))
---------------------------------------------------

