#!/usr/bin/env python
# coding: utf-8

# In[22]:


from __future__ import division
import nltk,re,pprint
from bs4 import BeautifulSoup


# EBOOK

# In[21]:


#爬取读取古登堡的书
from urllib.request import urlopen
url = "http://www.gutenberg.org/cache/epub/730/pg730.txt"
raw=urlopen(url).read()
type(raw)
len(raw)


# In[10]:


raw[:70]


# In[11]:


raw=raw.decode('utf-8')#因为是type类型，所以解码~


# In[12]:


tokens=nltk.word_tokenize(raw)#分词
type(tokens)
len(tokens)
tokens[:10]#不知道为啥害这样？


# In[13]:


text=nltk.Text(tokens)#变为nltk text，可以使用一些函数直接处理了~
text.collocations()


# In[14]:


#修剪使得文本就是从第一张到结束
raw.find("CHAPTER I")


# In[15]:


raw.rfind("END OF THIS PROJECT GUTENBERG EBOOK OLIVER TWIST")


# In[16]:


raw=raw[6255:917163]


# In[19]:


raw.find('CHAPTER I')
type(raw)
with open("Oliver Twist.txt",'w',encoding='utf-8') as f:
    f.write(raw)


# HTML
# 
# HTML→ASCII→Text→Voc
# 
# 爬取页面→清洗html保留文本→分词→生成Text(可以用text相关函数)→sort（单词）
# 
# 流程：打开网址链接，读取HTML内容，去除We open a URL and read its HTML content, remove the markup
# and select a slice of characters; this is then tokenized and optionally converted into an nltk.Text
# object; we can also lowercase all the words and extract the vocabulary.

# In[23]:


#获取网址+爬取
from urllib.request import urlopen
url = "https://intelligent-information.blog/en/augmented-translation-puts-translators-back-in-the-center/"
html = urlopen(url).read()
html[:70]


# In[24]:


#编码解码
type(html)
html=html.decode()
type(html)


# In[34]:


#清洗语料获得纯文本
#raw=nltk.clean_html(html)-不成了,用bs4提供的函数就好
# http://www.crummy.com/software/BeautifulSoup
raw=BeautifulSoup(html).get_text()
tokens=nltk.wordpunct_tokenize(raw)
#print(tokens)
#print(type(tokens))
raw1=raw[750:23506]
#print(raw1)
text=nltk.Text(tokens)
words=[w.lower()for w in text]
vocab = sorted(set(words))
print('word:',vocab,len(words),'++',len(vocab))
print('token:',tokens,len(tokens))


# In[19]:


tokens=tokens[96:399]
tokens
word=[i for i in tokens if i !=')']


# In[30]:


text=nltk.Text(tokens)
text.concordance('translation')


# In[24]:


#print(text)
#for word in text:
    #print(word)
from nltk.book import *    
wordfeq=FreqDist(tokens)
wordfeq


# In[28]:


wordset=set(tokens)
wordset


# In[26]:


print(len(wordset),len(tokens))


# - RSS Feeds(博客啥的，用http://feedparser.org/ 处理，可以做语料
# - search engine
# - Local Files

# In[6]:


import os
os.listdir('.')


# In[9]:


f = open('test.txt','r',encoding='utf-8')
for line in f:
    print(line.strip())#去除/n


# In[17]:


import nltk
path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
raw = open(path, 'r').read()
print(raw)
print('---------------------------------------')
for line in raw:
    print(line.strip()


# In[20]:


s = input("Enter some text: ")
print ("You typed", len(nltk.word_tokenize(s)), "words.",type(s))


# 一些区分

# In[36]:


rawtest='This is what I want to say. Jay had never told me about your experiences, so I quit.'
tokenstest=nltk.wordpunct_tokenize(rawtest)
tokenstest2=nltk.word_tokenize(rawtest)
print('punct',tokenstest,'nopunct',tokenstest2)


# In[ ]:




