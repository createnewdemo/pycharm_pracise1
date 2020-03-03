# -*- coding: gbk -*-
import requests


def get_news():
    # 这里是把今日糍粑每日一句中拿过来的信息发送给你朋友
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['note']
    print(contents)
    print(translation)
    # return contents,translation


get_news()
