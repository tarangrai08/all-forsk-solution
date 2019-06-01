# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:03:50 2019

@author: Rai
"""

Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.




import numpy as np
import pandas as pd

dataset = pd.read_csv('Female_Stats.csv')

features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values


features = features.reshape(-1,1)

--------------------------------------------------------------------------------------------
## 2 part

features = dataset.iloc[:, 1].values


features = features.reshape(-1,1)


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
print (regressor.coef_)
----------------------------------------------------------------------------------------------
## 3 part

features = dataset.iloc[:, 2].values


features = features.reshape(-1,1)


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
print (regressor.coef_)















