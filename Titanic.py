
# coding: utf-8

# In[6]:
import os
os.getcwd()
address ='C:\\Users\\jren\\Desktop\\Python\\Titanic'
os.chdir(address)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
# In[12]:
df = pd.read_csv('train.csv')
# In[13]:
df.head(5)
df.describe()


# In[24]:


# check null value
df.isnull().sum()


# In[44]:


# check value category
df.groupby('Pclass').sum()


# In[48]:


pd.

