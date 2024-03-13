#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


import csv


# In[9]:


mydata = pd.read_csv(r'C:\Users\Kwame Generale\Downloads\CardioGoodFitness.csv')


# In[10]:


mydata.head()


# In[11]:


mydata.describe(include="all")


# In[12]:


mydata.info()


# In[13]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

mydata.hist(figsize=(20,30))


# In[14]:


import seaborn as sns

sns.boxplot(x="Gender", y="Age", data=mydata)


# In[15]:


pd.crosstab(mydata['Product'],mydata['Gender'] )


# In[17]:


pd.crosstab(mydata['Product'],mydata['MaritalStatus'] )


# In[18]:


sns.countplot(x="Product", hue="Gender", data=mydata)


# In[19]:


pd.pivot_table(mydata, index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'], aggfunc=len)


# In[20]:


pd.pivot_table(mydata,'Income', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])


# In[21]:


pd.pivot_table(mydata,'Miles', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])


# In[22]:


sns.pairplot(mydata)


# In[23]:


mydata['Age'].std()


# In[24]:


mydata['Age'].mean()


# In[25]:


sns.distplot(mydata['Age'])


# In[26]:


mydata.hist(by='Gender',column = 'Age')


# In[27]:


mydata.hist(by='Gender',column = 'Income')


# In[28]:


mydata.hist(by='Gender',column = 'Miles')


# In[29]:


mydata.hist(by='Product',column = 'Miles', figsize=(20,30))


# In[31]:


corr = mydata.corr()


# In[32]:


corr


# In[33]:


sns.heatmap(corr, annot=True)


# In[ ]:




