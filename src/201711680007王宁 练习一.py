#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[]
for i in range (26):
    B=chr(ord('a')+i-32)
    b=chr(ord('a')+i)
    t = (B,b)
    list.append(t)
    print("{}-{}".format(B,b))


# In[ ]:




