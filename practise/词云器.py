import jieba
import wordcloud
from imageio import imread

mask = imread("中国地图.png")
f = open("2019-nCoV.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = "".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", \
                        width=1000, height=700, background_color="white", \
                        stopwords={"治法", "临床表现", "主症", "结合", "PCR", "2012第二版"}, mask=mask, \
                        scale=10, max_words=30)
w.generate(txt)
w.to_file("2019-nCoV1.png")
