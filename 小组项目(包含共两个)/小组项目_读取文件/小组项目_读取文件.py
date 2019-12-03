#读取压缩包 books.zip中的文本文件，将每个文件的中文和英语分别抽取出来，
#并分别统计每个文件中不同中文词汇与不同英文单词出现的次数，
#将统计结果保存到csv文件中，每个txt文件对应一个csv文件结果。
import re
import os
import os.path
import jieba#用于中文分词
import csv #用于写入csv文件
import string
rootdir = "D:\大三\python\文件读取IO"#被读取文件们所在目录
#创建中文停用词表，这两个表是网上下载的，直接存在了D:\大三\python\homework\
def stopwordslist():
    stopwords = [line.strip() for line in open('D:\大三\python\homework\stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords
def stopwordslisten():
    stopwords = [line.strip() for line in open('D:\大三\python\homework\stopwordsen.txt').readlines()]
    return stopwords
dict={}


for parent,dirnames,filenames in os.walk(rootdir):#开始逐个遍历
    for filename in filenames:
        #print(filename)
        file_obj=open(rootdir+'\\'+filename,'r')#开始读取单个文件
        contents = file_obj.read()#获取文件内容
        #for p in string.punctuation:
        #    contents= contents.replace(p," ")
        #contents = contents.replace('，', ' ')
        contents = contents.replace('．', ' ')
        contents=re.sub(r'[！. *,，!…？?.""“：”；:;\']',' ',contents)#标点替换成空格
        #print(contents)
        enp = re.compile(r'[a-zA-Z,\u0020]')#Unicode匹配英文
        chp = re.compile(r'[\u4e00-\u9fa5,{0,}$]')#Unicode匹配中文,数字
        en = "".join(enp.findall(contents.lower()))#获取到的英文内容
        #print(en)
        ch = "".join(chp.findall(contents))#获取到的中文内容
        #开始中文分词+词频统计
        segmentsch={}#用来盛放读出的词
        seg_list = jieba.cut(ch,cut_all=False)#分词词表
        stopwords=stopwordslist()#网上找的停用词表
        for word in  seg_list:
            if word not in stopwords:
                segmentsch[word]=1+segmentsch.get(word,0)#词频统计
        word_sort_ch=sorted(segmentsch.items(),key=lambda x:x[1],reverse=True)
        csvfile = open("Zh"+filename+".csv","w")  #写入CSV
        writer = csv.writer(csvfile)
        writer.writerow(['单词', '词频'])
        writer.writerows(word_sort_ch)
		#开始英文分词+词频统计
        segmentsen={}#用来盛放读出的英文词
        stopwordsen=stopwordslisten()#网上找的停用词表
        seg_list=en.split()#英文分词
        for word in  seg_list:
            if word not in stopwordsen:
                segmentsen[word]=1+segmentsen.get(word,0)
        word_sort_en=sorted(segmentsen.items(),key=lambda x:x[1],reverse=True)#按照词频来排序
        csvfile = open("En"+filename+".csv","w")  #写入CSV 
        writer = csv.writer(csvfile)
        writer.writerow(['单词', '词频'])
        writer.writerows(word_sort_en)

csvfile.close()
file_obj.close()




