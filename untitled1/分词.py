#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 22:24
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 分词.py
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#读取数据
with open('threekingdoms.txt','r',encoding='UTF-8') as f:  # 打开新的文本
    text = f.read()  # 读取文本数据
len(text)
#全部字符变成小写字符
text = text.lower()
#读取停用词，创建停用词表
stwlist = [line.strip() for line in open ('u8stop.txt',encoding='utf-8').readlines()]
#先进行分词
words = jieba.cut(text,cut_all = False,HMM = True)
#cut_all:是否采用全模式
#去停用词,统计词频
word_ = {}
res = []
for word in words:
    if word.strip() not in stwlist:
        if len(word) > 1:
            if word != '\t':
                if word != '\r\n':
                    #计算词频
                    res.append(word)
                    if word in word_:
                        word_[word] += 1
                    else:
                        word_[word] = 1

#将词汇和词频以元组的形式保存
word_freq = []
for word,freq in word_.items():
    word_freq.append((word,freq))
#进行倒序排列
word_freq.sort(key = lambda x:x[1],reverse = True)

#查看前100个结果
for i in range(30):
     word,freq =word_freq[i]
     print('{0:10}{1:5}'.format(word,freq))

img_txt = []
with open('shuchu.txt', 'w') as fw:  # 将结果保存到shuchu文件
    for word, freq in word_freq:
        fw.write('%s,%d\n' %(word,freq))
        img_txt.append(word)




# import numpy as np
# from PIL import Image
# import jieba
# from wordcloud import ImageColorGenerator, wordcloud, WordCloud
# import matplotlib.pyplot as plt
# f = open("threekingdoms.txt","r",encoding="utf-8")
# t = f.read()
# f.close()
# image=np.array(Image.open('1.jpg'))
# font = "C:/Windows/Fonts/simfang.ttf"
# result = jieba.cut(t)
# txt = "".join(result)
# print(txt)
# myCloud = WordCloud(scale=4,font_path=font,mask=image,background_color='white',max_words = 30,max_font_size = 60,random_state=20).generate(txt)
# plt.imshow(myCloud)
# plt.axis("off")
# plt.show()
# myCloud.to_file('cloud.jpg')