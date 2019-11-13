#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
url='https://news.sina.com.cn/'
strhtml=requests.get(url)
print(strhtml)


# In[17]:


import requests        #导入requests包
import json
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
From_data={'i':"word",'from':'zh-CHS','to':'en','smartresult':'dict','client':'fanyideskweb','salt':'15477056211258','sign':'b3589f32c38bc9e3876a570b8a992604','ts':'1547705621125','bv':'b33a2f3f9d09bde064c9275bcb33d94e','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_REALTIME','typoResult':'false'}
    #请求表单数据
response = requests.post(url,data=From_data)
    #将Json格式字符串转字典
content = json.loads(response.text)
print(content)
#error


# In[73]:


import requests
from bs4 import BeautifulSoup
i=1;
url = 'http://news.sina.com.cn/china/'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'UTF-8'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')

#遍历每一个class=news-item的节点
for news in soup.select('.right-content'):
    #print(news)
    #print
    ul=news.select('ul')
    l=len(ul)
    print(l)
    if l >0:
        #i++ python貌似不支持？
        title=(ul[l-i].text)
        href=(ul[l-i].select('li')[0])
        print(title)
    i+=1
#ul标签下不是都能爬下来，有问题，爬取了两条标题


# In[ ]:




