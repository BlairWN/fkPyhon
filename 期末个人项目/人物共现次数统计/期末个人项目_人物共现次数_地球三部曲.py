#!/usr/bin/env python
# coding: utf-8

# In[1]:


#《地球三部曲》：由于jieba分词标注nr不全为名字且有很多名字未被识别，因此自己列了名字列表
import codecs
import jieba
import os
from jieba import posseg
import csv


class Earth(object):

    # 初始化
    def __init__(self):
        # 姓名字典
        self.names = {}
        # 关系字典
        self.relationships = {}
        # 每段内人物关系
        self.lineNames = []
    
    def analyze_word(self):
        # 加载字典
        with codecs.open("D:\大三\python\homework\week13课后作业\The_three_body_problem_full\《地球往事三部曲》全集.txt", "r", "utf-8") as f:
            for line in f.readlines():
                # 分词返回词性，本来想直接用nr控制判断 但是发现jieba标注的不够正确 所以就用了任务名称列表
                poss = posseg.cut(line)
                # 为新读取的一段添加人物关系
                self.lineNames.append([])
                for w in poss:
                    if w.word not in ['汪淼', 'aa', '李瑶', '豆豆', '史强', '常伟思', '斯坦顿', '杨冬', '丁仪', '申玉菲', '魏成', '潘寒', '叶文洁', '楠楠', '洋洋', '咪咪', '沙瑞山', '叶哲泰', '邵琳', '叶文雪', '白沐霖', '马钢', '程丽华', '雷志成', '杨卫宁', '齐猎头', '大凤', '徐冰冰', '唐红静', '伊文斯', '林云', '智子', '罗辑', '麦克·伊文斯', '吴岳', '章北海', '雷德尔', '琼斯', '乔治·菲兹罗', '张援朝', '杨晋文', '苗福全', '贾维彬', '常伟思', '史强', '史晓明', '加尔诺夫', '白蓉', '坎特', '萨伊', '艾伯特·林格', '伽尔宁', '艾伦', '麦克', '井上宏一', '威廉·科兹莫', '庄颜', '哈里斯', '张翔', '张卫明', '张延', '晓虹', '威尔逊', '凯瑟琳', '熊文', '本·乔纳森', '郭正明', '东方延续', '肯博士', '罗宾逊', '列文', '井上明', '西子', '赵鑫', '李维', '蓝西', '斯科特', '杨冬', '云天明', '老李', '张医生', '胡文', '程心', '萨伊', '何博士', '米哈伊尔·瓦季姆', '托马斯·维德', '于维民', '柯曼琳', '乔依娜', '尼尔·斯科特', '塞巴斯蒂安·史耐德', '鲍里斯·洛文斯基', '卡尔·乔伊娜', '毕云峰', '曹彬', '伊万·安东诺夫', 'A·J·霍普金斯', '韦斯特博士', '戴文中尉', '朴义君少校', '伊万', '艾克', '薇拉', '刘晓明', '关一帆', '弗雷斯', '詹姆斯·亨特', '秋原玲子', '约瑟夫·莫沃维奇', '褚岩', '卓文', '深水王子', '冰沙王子', '露珠公主', '针眼画师', '空灵画师', '宽姨', '长帆护卫', '广田老师', '巴勒莫', '杰森', '威尔纳', '阿历克塞·瓦西里', '高way', '布莱尔', '白Ice']:
                        # 如果没有出现在任务名称列表里就过滤掉
                        continue
                    
                    self.lineNames[-1].append(w.word)#添加name
                    if self.names.get(w.word) is None:#如果name里没有这个name
                        self.names[w.word] = 0#那就设置成0个
                        self.relationships[w.word] = {}
                    # 人物出现次数+1
                    self.names[w.word] += 1#要是有就直接加
    
    def analyze_relationship(self):
        for line in self.lineNames:
            for name1 in line:
                for name2 in line:
                    if name1 == name2:
                        continue
                    if self.relationships[name1].get(name2) is None:
                        # 两个人物第一次共同出现 初始化次数
                        self.relationships[name1][name2] = 1
                    else:
                        # 两个人物共同出现 关系+1
                        self.relationships[name1][name2] += 1
    def generate_gephi(self):
        # 人物权重
        with codecs.open("D:\大三\python\homework\week13课后作业\The_three_body_problem_full\人物出现频数.csv", "w", "gbk") as f:
            f.write("Name Weight\r\n")
            name_sort_ch=sorted(self.names.items(),key=lambda x:x[1],reverse=True)
            for name, times in name_sort_ch:
                f.write(name + " " + str(times) + "\r\n")

        # 人物关系
        with codecs.open("D:\大三\python\homework\week13课后作业\The_three_body_problem_full\人物共现频数.csv", "w", "gbk") as f:
            f.write("Name1 Name2 Weight\r\n")
            for name, edge in self.relationships.items():
                for v, w in edge.items():
                    if w > 3:
                        f.write(name + " " + v + " " + str(w) + "\r\n")
#主函数
earth=Earth()
earth.analyze_word()
earth.analyze_relationship()
earth.generate_gephi()


# In[ ]:




