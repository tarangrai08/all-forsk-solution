"""
Created on Wed May 22 10:47:21 2019

@author: Rai
"""

"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""




from bs4 import BeautifulSoup
import requests


wiki = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(wiki).text


soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)



A=[]
B=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State/Territory","National Share (%)"]
col_data = OrderedDict(zip(col_name,[A,B]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
  
higest_share = df.loc[0:5]

higest_share = df.loc[0:5,["State/Territory","National Share (%)"]]

labels = ('rajasthan','mp','maharastra','up','gujarat','karnataka')
sizes = [10.41,9.37,9.36,7.33,5.96,5.83]
colors = ['gold', 'yellowgreen', 'red', 'lightskyblue','brown','purple']
explode = (0.1, 0.2, 0.1, 0.2, 0.1, 0.2)  # explode 1st slice



plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)


plt.axis('equal')  

