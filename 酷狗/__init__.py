# -*- coding: gbk -*-
import pymysql
import requests
from lxml import etree
import re
def parseOnePage():
    url = "https://www.kugou.com/fmweb/app/js/main.js"
    r = requests.get(url)
    r.encoding= 'utf-8'
    info = re.findall(r'var radioType = (.*)',r.text)[0]


    print(info)
    #print(r.text)
parseOnePage()