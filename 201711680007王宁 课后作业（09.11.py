#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1.计算10000以内所有2,3,4,5的倍数的正整数的和并分别打印出来
a=[0,0,0,0]
for i in range (1,10001):
    if(i%2==0):
       a[0]=a[0]+i
    if(i%3==0):
        a[1]=a[1]+i
    if(i%4==0):
        a[2]=a[2]+i
    if(i%5==0):
        a[3]=a[3]+i
print(a)
    


# In[23]:


#将可打印的ascii码全部放入一个数组中，并以每行20个的格式打印出来 
a=0;
for i in range (32,128):
    a=a+1
    print(chr(i),end='')
    if(a%20==0):
        print("\n",end="")


# In[ ]:




