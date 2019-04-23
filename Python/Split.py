
# coding: utf-8

# In[14]:

import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

path = '/Users/avinashbarnwal/Desktop/Machine Learning/Python Code/Practice/'
os.chdir(path)

data = pd.read_csv("split.csv")
data['id_1'], data['id_2'] , data['id_3'] = data['ID'].str.split('_',2).str
data['id_1_2'] = data[['id_1','id_2']].apply(lambda x : '_'.join(x),axis=1)

data.head()

