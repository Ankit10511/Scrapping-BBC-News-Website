#!/usr/bin/env python
# coding: utf-8

# In[21]:


from bs4 import BeautifulSoup
import requests 
import pandas as pd
from pandas import Series, DataFrame


# In[4]:


url = "https://www.bbc.com/news"


# In[7]:


# Call API
result = requests.get(url)
print(result.content)


# In[8]:


soup = BeautifulSoup(result.content, 'lxml')
print(soup)


# In[14]:


content = soup.find(class_='nw-o-news-branding')
print(content)


# In[16]:


content1 = soup.findAll('div')
print(content1)


# In[17]:


print(len(content1))


# In[24]:


summary = soup.find(class_='gs-u-pb++ gs-u-box-size')
l = summary.findAll('h2')
series = [ele.get_text() for ele in l]
print(series)


# In[ ]:




