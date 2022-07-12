#!/usr/bin/env python
# coding: utf-8

# https://www.youtube.com/watch?v=R67XuYc9NQ4&ab_channel=MedallionDataScience

# In[1]:


# script to adjust cell width 
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>")) # just adjust the % to suit yourself


# In[26]:


pip install fredapi 


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# In[3]:


from fredapi import Fred
key = ''
pd.options.display.max_columns = 600
# dunno how many columns will be displayed. This allows to display many columns


# In[4]:


# 1. Create the Fred Object to pull in the data we need
fred = Fred(api_key=key)


# In[5]:


# 2. once the fred object is created, we can search for the economic data
fred.search('yields') # just type in what you need to search, unemployment, manufacturing etc. 


# In[31]:


# pull the raw data
series = fred.get_series('BAMLH0A0HYM2') # to pull data, we need to put in the series id
#series.info()
column_name = 'yields'
series.index.name = 'Date'
series = pd.DataFrame(series, columns = {column_name})
series


# In[15]:


# get user input to save above data into excel sheet if needed
print('Do you want to save the data to excel?')
savedata_excel = str(input("Enter y or n: "))
if savedata_excel == 'y':
    file_name = str(input("Enter file name: ")) #name the file as fit
    filename= file_name+'.xls'
    series.to_excel(filename,sheet_name=column_name)
    print('Data saved to excel! Download the sheet if you wish.')
elif savedata_excel == 'n':
    print()
    print('You have opted not to save the data')


# In[32]:


# plot the data
fig = px.line(series,x=series.index,y=series.yields)
fig.show()


# In[ ]:




