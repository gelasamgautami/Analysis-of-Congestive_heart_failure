
# coding: utf-8

# In[1]:


import numpy as np

import matplotlib.pyplot as plt

import pandas as pd



# In[2]:


dataset = pd.read_csv("hospital.csv")

X = dataset.iloc[:,:1].values

y = dataset.iloc[:,1].values



# In[3]:



from sklearn.cross_validation import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state = 0)



# In[4]:



from sklearn.linear_model import LogisticRegression



# In[5]



logmodel=LogisticRegression()



# In[6]:



logmodel.fit(X_train,y_train)



# In[11]:



predictions=logmodel.predict(X_test)



# In[8]:



from sklearn.metrics import classification_report



# In[12]:



classification_report(y_test,predictions)



# In[13]:



from sklearn.metrics import confusion_matrix



# In[14]:



confusion_matrix(y_test,predictions)



# In[15]:



from sklearn.metrics import accuracy_score



# In[16]:



accuracy_score(y_test,predictions)

