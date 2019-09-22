#!/usr/bin/env python
# coding: utf-8

# In[2]:


#练习二
#1.在当前工作文件夹下创建50个以test为前缀，不重名的文件夹。
import os
os.getcwd()
for i in range (50):
    os.mkdir("test"+str(i))

