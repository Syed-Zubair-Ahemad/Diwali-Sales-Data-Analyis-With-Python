#!/usr/bin/env python
# coding: utf-8

# first install the function wll be use 

# In[2]:



get_ipython().system(' pip install numpy')


# In[3]:


h    h ny  pip install pandas


# In[4]:


get_ipython().system(' pip install seaborn')


# In[6]:


get_ipython().system(' pip install matplotlib.pyplot')


# In[7]:


pip install matplotlib


# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(r'C:\Users\Syed Usaid\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali sales data.csv',encoding = 'unicode_escape')


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


df.info


# In[9]:


df.drop(['Status','unnamed1'] ,axis =1 , inplace = True)


# In[10]:


df.info()


# In[27]:


pd.isnull(df)


# In[13]:


pd.isnull(df).sum()


# In[12]:


df.dropna(inplace=True)


# In[31]:


df['Amount']=df['Amount'].astype('int')


# In[32]:


df['Amount'].dtypes 


# In[33]:


df.columns


# In[ ]:





# In[ ]:





# In[ ]:





# # Anlysis

# In[16]:


sns.countplot(x='Gender',data=df)


# In[18]:


ax= sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by ='Amount' , ascending =False)


# In[27]:


df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by ='Amount' , ascending =False)


# In[35]:


sales_gen= df.groupby(['Gender'], as_index = False )['Amount'].sum().sort_values(by = 'Amount',ascending = False)
xz=sns.barplot(x='Gender',y='Amount',data =sales_gen)
for bars in xz.containers:
    xz.bar_label(bars)


# In[38]:


ax=sns.countplot(data=df,x='Age Group',hue ='Gender')


# In[40]:


ax=sns.countplot(data=df,x='Age Group',hue ='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[ ]:





# # Age Group 

# In[49]:


sales_age=df.groupby(['Age Group'],as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)
ax=sns.barplot(x= 'Age Group',y='Amount',data=sales_age)
for bars in ax.containers:
    ax.bar_label(bars)


# # State
# 

# In[57]:


sales_sate=df.groupby(['State'],as_index =False)['Amount'].sum().sort_values(by='Amount',ascending=False)
ax=sns.barplot(y='State',x='Amount',data=sales_sate)
for bars in ax.containers:
    ax.bar_label(bars)


# In[64]:


sales_sate=df.groupby(['State'],as_index =False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(8)
sns.set(rc={'figure.figsize':(15,5)})
ax=sns.barplot(x='State',y='Amount',data=sales_sate)


# In[ ]:





# In[67]:


order_sate=df.groupby(['State'],as_index =False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(8)
sns.set(rc={'figure.figsize':(15,5)})
ax=sns.barplot(x='State',y='Orders',data=sales_sate)


# In[75]:


ax=sns.countplot(data=df, x='Marital_Status')


# In[83]:


Slales_state=df.groupby(['Marital_Status','Gender'],as_index=False).sum().sort_values(by ='Amount',ascending=False)
sns.barplot(data=Slales_state,x='Marital_Status',y='Amount',hue='Gender')


# In[99]:


sns.set(rc={'figure.figsize':(15,5)})
ax=sns.countplot(data=df,x='Occupation')

for bar in ax.containers:
    ax.bar_label(bars)


# In[98]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Product_Category')
for bar in ax.containers:
    ax.bar_label(bars)


# In[103]:


order_sate=df.groupby(['Product_Category'],as_index =False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(8)
sns.set(rc={'figure.figsize':(15,5)})
ax=sns.barplot(x='Product_Category',y='Amount',data=order_sate)


# In[106]:


order_sate=df.groupby(['Product_ID'],as_index =False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(8)
sns.set(rc={'figure.figsize':(15,5)})
ax=sns.barplot(x='Product_ID',y='Orders',data=order_sate)


# In[105]:


df.columns

