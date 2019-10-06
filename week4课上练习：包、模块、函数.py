#!/usr/bin/env python
# coding: utf-8

# In[47]:


#vim myModule.py
count=1

def func():
        global count
        count=count+1
        return count


# In[4]:


#vim a.py
from vim import myModule
print("count=", myModule.func())
myModule.count=10
print("count=",myModule.count)

from vim import myModule
print("count=",myModule.func())


# In[15]:


#filter函数的使用（过滤作用，留下第二个变量中符合第一个函数要求的变量
#filter（function，sequence），function可以是匿名函数或者自定义函数，
#它会对后面的sequence序列的每个元素判定是否符合函数条件，返回TRUE或者FALSE，从而只留下TRUE的元素；
#sequence可以是列表、元组或者字符串
def func(x):
    if (x>0):
        return (x)
print (filter(func,range(-9,10))) #调用filter函数，返回的是filter对象
print(tuple(filter(func,range(-9,10)))) #将filter对象转换为列表


# In[29]:


#map函数的使用（求一个序列或者多个序列进行函数映射之后的值
#map(function,iterable1,iterable2)，function中的参数值不一定是一个x，也可以是x和y，甚至多个；
#后面的iterable表示需要参与function运算中的参数值，有几个参数值就传入几个iterable
x = [1,2,3,4,5]
y = [1,2,3]
z = [7,8,0]
list(map(lambda x,y,z:(x*y)+z+2,x,y,z))
#输出列表中个数=最小个数


# In[56]:


#sys模块
import sys
#print(dir(sys),'\n')
print(sys.argv,'\n')     #命令行参数List，第一个元素是程序本身路径
print(sys.version,'\n')
print(sys.path,'\n')
sys.stdout.write('please:')


# In[55]:


#random 模块
import random
#print(dir(random))
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice(['tomorrow','v',1,(1,2,3),[4,5]]) )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
a=[1,3,5,6,7,(8,9),[10]]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)
print(random.sample([1, '23', [4, 5],'happy'], 3))#随机选择任意x个数字

