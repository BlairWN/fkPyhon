#!/usr/bin/env python
# coding: utf-8

# In[4]:


a='wangning';
a.split('n');
a


# In[5]:


a=[1,2,3,4,5];
a.append('hello');


# In[6]:


a


# In[7]:


a[3]=(2,3);
a


# In[17]:


for i in range(5):
    print (a[i]);

a.extend([4,3,2])
a


# In[ ]:





# In[ ]:


b=set([1,(9,110),2,(3,4),3,4,5,(7,8)]);
b


# In[4]:


#推导式
a=[i*2 for i in range(10)]
a


# In[3]:


a=[]
for i in range(10):
    a.append(i*2)
a


# In[5]:


#二维数组
a=[[1,2,3],[0,0,0],[4,5,6]]
a


# In[6]:


a=[]
for i in range(10):
    b=[]
    for j in range(10):
        b.append(j)
    a.append(b)
a


# In[8]:


#推导式=>简写方式
b=[[i for i in range(10)] for j in range(10)]
b


# In[9]:


b=[[i for i in range(i)] for j in range(10)]
b
#函数变量作用域


# In[18]:


a=[i for i in range(10)]
b=[chr(ord('a')+i)for i in range (10)]
b


# In[15]:


a


# In[20]:


#字典 打包遍历=> k，v分别对应b，a 快速赋值（先说结果再说过程
c={k:v for k,v in zip(b,a)}
c


# In[31]:


list(c.keys())
list(c.values())


# In[34]:


for k,v in c.items():
    print(k,v)


# In[35]:


b


# In[36]:


a


# In[40]:


for b1,a1 in zip(b,a):
    print(b1,'\t',a1)


# In[38]:


#定义列举
for i,v in enumerate(b):
    print(i,'\t',v)


# In[41]:


c = ['A','C','GOOD','BAG']
for x,a in enumerate(c):
    print(x,a)


# In[48]:


c={}
c=dict()
c


# In[50]:


type(c)


# In[51]:


c={'a':1,'b':2}
c={0:'a',1:'b'}
a=[1,2,3,4]
b=(1,2,3)
c=set(['a','b','c'])
d={'k1':a,'k2':b,'k3':c}
d


# In[52]:


d={'k1':{'k2':2},'k3':[{'k4':5}]}
d
#嵌套定义


# In[53]:


#pprint函数库了解一下，json
import json
d['k1']


# In[54]:


d['k1']['k2']


# In[55]:


json.dumps(d)


# In[56]:


json.dumps(d,indent=4)


# In[58]:


print(json.dumps(d,indent=4))
#嵌套结构


# In[60]:


#os内置库函数交互式编程
import os
str(dir(os))


# In[61]:


os.system


# In[62]:


os.listdir


# In[64]:


os.mkdir


# In[70]:


#练习二1
#1.在当前工作文件夹下创建50个以test为前缀，不重名的文件夹。
#2.统计一个文件个数超过20的文件夹中（比如C:\Windows\System32），
#不同类型（后缀）文件的个数，并打印出来(选做)。
os.getcwd()
for i in range (50):
    os.mkdir("test"+str(i))


# In[81]:


#练习二2提示
a='abcd.txt'
a[4:]


# In[88]:


#python内置函数
import os,math
def afuc(x):
    a=10
    x=x+str(a)
    print(x)
w='happy'
afuc(w)
str(dir(math))


# In[90]:


help(os.walk)


# In[100]:


for root,dirs,files in os.walk('./',topdown=False):
        print(root)
        print(dirs)
        print(files)


# In[ ]:




