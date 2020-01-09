#!/usr/bin/env python
# coding: utf-8

# In[74]:


#分别统计His_dark_meterials_full_en.zip和The_three_body_problem_full.zip 中所有不同类型词汇的分布比例。
#比如对于前者，统计其中英文单词中名词、形容词、副词等等占所有词汇的百分比；
#对于后者，统计中文中各类词汇的占比。
import re
import xlwt
import csv
import jieba
import jieba.posseg as pseg
from jieba import analyse
from collections import Counter


# In[52]:


def stopwordslist():
    stopwords = [line.strip() for line in open('D:\大三\python\homework\stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords
with open("D:\大三\python\homework\week13课后作业\The_three_body_problem_full\《地球往事三部曲》全集.txt",encoding='UTF-8')as f:
    text=f.read().encode()
#print(type(text))
text1=text.decode('utf-8')
#print(type(text1))

#过滤非中文字符
results=re.compile('[\u4e00-\u9fa5]+').findall(text1)
print(results)
print(len(results))
textstr=''.join(results)


# In[53]:


print(textstr)


# In[54]:


#词性标注
words=pseg.cut(textstr)
print(type(words))


# In[55]:


#未去停用词版本：
word_list=[]
for w in words:
    print (w)
    word_list.append(w)
    
print(type(word_list))
print(type(word_list[0]))


# In[56]:


#去除空格
n = -1
for (k,v) in word_list:
    n+=1
    if k is ' ':
        word_list.remove(word_list[n])
print(word_list)


# In[59]:


#词频统计
dic={}
for item in word_list:
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1
print(dic)
key=list(dic.keys())
value1=list(dic.values())
print(key)
print(value1)


# In[105]:


#词性整合
list_words = []
pos = {}
list_pos = []
n = -1
for (k,v) in key:
    n+=1
    list_words.append(k)
    list_pos.append(v)
    if v not in pos:
        pos[v] = 1
    else:
        pos[v] += 1

print(list_words)
print(list_pos)
print(pos)
row_list=len(list_words)
print(row_list)
#print(list_pos)
#print(value1)


# In[106]:


#写入数据xls--词频+词性统计
workbook = xlwt.Workbook(encoding='utf-8')
sheet1=workbook.add_sheet(r'sheet1',cell_overwrite_ok=True)
#写入单元格
for row in range(row_list):
    for Column in range(3):
        if Column ==0:
            sheet1.write(row,Column,list_words[row])
        elif Column ==1:
            sheet1.write(row,Column,list_pos[row])
        else:
            sheet1.write(row,Column,value1[row])
workbook.save('地球三部曲_词性分布.xls')


# In[123]:


#词性分布计算--词性/总数
#print(pos)
n=0
for v in pos:
    #print(pos[v])
    n = n+pos[v]

#分布统计：
x=0
for v in pos:
    pos[v]=pos[v]/n


word_sort_ch=sorted(pos.items(),key=lambda x:x[1],reverse=True)
csvfile = open("地球三部曲分布词性.csv","w")  #写入CSV
writer = csv.writer(csvfile)
writer.writerow(['单词', '词频'])
writer.writerows(word_sort_ch)
pos


# In[ ]:




