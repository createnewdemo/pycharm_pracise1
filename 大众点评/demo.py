
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 18:08
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo.py
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re


from html.parser import HTMLParser #导入html解析库
from lxml import html
def get_html():
    cookies = {
        'dplet': '04658f527fc38c907c182c03ff24ebdc',
        'dper': 'd4584ef13ca9733ab43de66a77ce8b5ed01a7512542ff2e238ea2cc349fde9454365ca76a4f065b4213aa10c2c9f5d3189c14daed57b137a4e3a4f8bf91a3b76',
        'll': '7fd06e815b796be3df069dec7836c3df',
        'ua': 'dpuser_8030456887',
        'ctu': '8b74917f26973cac7131d6146b75c32131c0da039c3670bcb7140cac0216c5b4',
        'uamo': '17190199811',
        '_lxsdk_cuid': '171879b3a00c8-0edc4eca668766-3a614f0b-1fa400-171879b3a00c8',
        '_lxsdk': '171879b3a00c8-0edc4eca668766-3a614f0b-1fa400-171879b3a00c8',
        '_hc.v': '68cbc84f-ac24-cb19-b9b4-ba8475424f57.1587118030',
        '_lxsdk_s': '171879b3a01-9e7-fa9-249%7C%7C173',
    }
    headers = {
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }
    response = requests.get('http://www.dianping.com/shop/113123589/review_all', headers=headers, cookies=cookies)
    response.encoding = "utf-8"
    r = response.text
    return r
def get_info():
    import html
    r = get_html()
    xp = etree.HTML(r)
    divs = xp.xpath('//div[@class="main-review"]')[0]
    info_xml = divs.xpath('.//div[@class="review-words Hide"]')[0]
    result = etree.tostring(info_xml)
    pinglun_html = html.unescape(result.decode())
    #print(name2,type(name2))
    pinglun_text = pinglun_html.replace('<svgmtsi class="', ',').replace('"/>', ",").replace('">', ",")
    pinglun_list = [x for x in pinglun_text.split(",") if x != '']
    print(pinglun_list)

    return result
    #print(xp)
get_info()