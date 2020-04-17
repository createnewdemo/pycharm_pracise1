#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 11:31
import numpy as np
from PIL import Image
import jieba
from wordcloud import ImageColorGenerator, wordcloud, WordCloud
import matplotlib.pyplot as plt
f = open("threekingdoms.txt","r",encoding="utf-8")
t = f.read()
f.close()
image=np.array(Image.open('1.jpg'))
font = "C:/Windows/Fonts/simfang.ttf"
result = jieba.cut(t)
txt = "".join(result)
myCloud = WordCloud(scale=4,font_path=font,mask=image,background_color='white',max_words = 30,max_font_size = 60,random_state=20).generate(txt)
plt.imshow(myCloud)
plt.axis("off")
plt.show()
myCloud.to_file('cloud.jpg')
