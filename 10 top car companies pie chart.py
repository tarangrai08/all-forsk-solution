# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:07:11 2019

@author: Rai
"""

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Automobile.csv")

series = df["make"].value_counts()

print (series.index[0:10])
print (series.values[0:10])

explode = (0.5,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:10], explode = explode, labels=series.index[0:10], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()