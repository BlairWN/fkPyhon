#!/usr/bin/env python
# coding: utf-8

# In[13]:


#九九乘法表
for i in range (1,10):
    for j in range(1,10):
        if(i>j):
            continue
        print("{}*{}={}".format(i,j,i*j),end="||")
    print('\n')

