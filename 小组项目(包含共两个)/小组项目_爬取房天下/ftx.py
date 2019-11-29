import requests
from bs4 import BeautifulSoup
import csv#将数据存入csv文件

def pachong(inputurl):
    req=requests.get(url=inputurl)#抓取页面
    req.encoding='gb2312'
    html=req.text
    bf=BeautifulSoup(html,"lxml")
    url=bf.find_all('div',class_='page')   
    div=bf.find_all('div',class_='nl_con clearfix')#楼盘信息
    
    #print(type(div[0]))
    x=BeautifulSoup(str(div[0]),"lxml")
    
    try:
        h=x.find_all('div',class_='kanesf')#特殊情况，新房已售出
        h[0]['class']='nhouse_price'#将属性换掉
    except:
        pass
    y=x.find_all('div',class_='nhouse_price')#楼盘价格
    a=x.find_all('div',class_='address')#楼盘地址
    #print(type(y[0]))
    b=BeautifulSoup(str(a),"lxml")
    c=b.find_all('a')
    #print(y[1].label.string)#存在有价格待定的格式
    
    try:
        for i in range(20):#一个页面差不多有20个房价信息，排除最后一页
            z=y[i].get_text()
            '''if y[i].span:
                e=y[i].span.string
            else:
                e=y[i].label.string+y[i].i.string'''
            
            if y[i].em:
                #if str(y[i].em.string)[-2:]=='�O' or str(y[i].em.string)[-3:-1]=='�O':
                if z[-3:-1]=='�O' or z[-4:-2]=='�O':#替换掉乱码情况
                    z=z.replace('�O','m^2')
                
            writer.writerow([str(c[i]['title']),z])#写入csv文件中
            #print(c[i]['title'],z)
    
    #csvfile.close()
    
    except:
        pass

target='https://newhouse.fang.com/house/s/?ctm=1.bj.xf_search.lpsearch_area.1'
req=requests.get(url=target)
req.encoding='gb2312'
furl='https://newhouse.fang.com'#url前缀
html=req.text

bf=BeautifulSoup(html,"lxml")
li=bf.find_all('li',class_='quyu_name dingwei')
lin=BeautifulSoup(str(li),"lxml")
link=lin.find_all('a')
location=['朝阳','海淀','丰台','西城','东城','昌平','大兴','通州','房山','顺义','石景山','密云','门头沟','怀柔','延庆','平谷','燕郊','北京周边']#手动总结这几个区，把它们的名字放在一个列表里面。
for i in range(1,19):
    csvfile=open(location[i-1]+'.csv','a+',newline='',encoding='GB2312')#创建一个写入csv
    writer=csv.writer(csvfile)
    writer.writerow(['具体位置','房价'])
    links=furl+link[i]['href']
    pachong(links)#爬取该网页第一页的信息
    req=requests.get(url=links)
    req.encoding='gb2312'
    html=req.text
    bf=BeautifulSoup(html,"lxml")
    url=bf.find_all('div',class_='page')
    #print(url[0])
    try:
        page=url[0].find_all('a')
        if len(page)>0:
            print(page[1:-2])
            for j in page[1:-2]:#page[1:-2]是接下来要爬取的页面
                nurl=furl+j['href']#收集此地区跳转页面url
                pachong(nurl)
    except:
        pass
    csvfile.close()#关闭csv