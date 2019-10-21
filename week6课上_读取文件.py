#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1.读取压缩包 books.zip中解压缩后的文本文件，以文件名为键，文件中文本的长度为值，组成一个字典
import os
import os.path
rootdir = "D:\大三\python\文件读取IO"
dict={}


for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        #print(filename)
        file_obj=open(rootdir+'\\'+filename,'r')
        contents = file_obj.read()
        words = contents.rstrip()
        num_words = len(words)
        dict[filename]=num_words
        #print(num_words)
file_object.close()
print(dict)


# In[16]:


#2. 将上述字典以json字符串的形式存入文本文件中
import json
json_str = json.dumps(dict)
with open('train.json', 'w') as json_file:
    json_file.write(json_str)


# In[14]:


#3. 将上述字典以pickle二进制形式存入文件中；
import pickle
pickle_file = open( 'train.pkl', 'wb')  
pickle.dump(dict,pickle_file)           
pickle_file.close()   

