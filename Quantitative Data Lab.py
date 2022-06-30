#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib


# In[3]:


file = 'file (1).csv'


# In[4]:


df = pd.read_csv('file (1).csv')
print(df.head())


# In[5]:


print(list(df))


# In[6]:


quant_col = 'Value'
mean = df[quant_col].mean()
print(mean)

median = df[quant_col].median()
print (median)

standard_deviation = df[quant_col].std()
print(standard_deviation)


# In[ ]:




