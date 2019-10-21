#!/usr/bin/env python
# coding: utf-8

# In[24]:


#在命令行下传递参数，参数为需要读取的文件的文件名；
#读取文件时使用异常处理的方法来解决不存在文件的异常情况
#分别将读取的文件中的中文和英文分离开来，另存为两个文件；  
import sys
import re
from sys import argv
rootdir =  "D:\大三\python\文件读取IO"
file_name=argv[1]
#print(file_name)

try:
    with open(rootdir+'\\'+file_name) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file' + file_name + ' does not exist.'
    print(msg)
else:
    words = contents.rstrip()#去除空格
    enp = re.compile(r'[\u0061-\u007a,\u00209]')#Unicode匹配英文
    chp = re.compile(r'[\u4e00-\u9fa5,\u0030-\u0039]')#Unicode匹配中文,数字
    en = "".join(enp.findall(words.lower()))
    ch = "".join(chp.findall(words))
    with open("En"+file_name,"w") as f:
        f.write(en)
    with open("Zh"+file_name,"w") as f:
        f.write(ch)


# In[ ]:





# In[ ]:




