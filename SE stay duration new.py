#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns


# In[13]:


import pickle
import math


# In[2]:


df = pd.read_csv('D:\Semester 4\AI\hotel_bookings.csv')
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
df.fillna(0, inplace = True)
df.head()


# In[3]:


correlation = df.corr()['total_nights'].abs().sort_values(ascending = False)
correlation


# In[4]:


df2 = pd.DataFrame()

df2['stays_in_week_nights']=df['stays_in_week_nights']
df2['stays_in_weekend_nights']=df['stays_in_weekend_nights']
df2['agent']=df['agent']
df2['is_repeated_guest']=df['is_repeated_guest']
df2['total_nights']=df['total_nights']
df2


# In[5]:


X=df2.drop('total_nights',axis=1)
y = df['total_nights']


# In[6]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)


# In[7]:


X.shape,y.shape


# In[8]:


y_train.head(), y_test.head()


# In[ ]:





# In[12]:


dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred_dtc = dtc.predict(X_test)

acc_dtc = accuracy_score(y_test, y_pred_dtc)
conf = confusion_matrix(y_test, y_pred_dtc)
clf_report = classification_report(y_test, y_pred_dtc)

print(f"Accuracy Score of Decision Tree is : {acc_dtc}")
print(f"Confusion Matrix : \n{conf}")
print(f"Classification Report : \n{clf_report}")


# In[14]:


pickle.dump(dtc,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


# In[ ]:




