# encoding: utf-8
# -*- coding: gbk -*-
# !/usr/bin/env python3
import pandas
import requests
import time, threading, queue
from bs4 import BeautifulSoup
import urllib
import re, csv
import pymysql
from lxml import etree
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
url = 'https://www.douban.com/search?cat=1001&q={}'
ip = []
num = 0


def one_book_url_list(book_name):
    global num
    # book_name=str(input('请输入所要查找的书籍名称/作者:'))
    b = urllib.parse.quote(book_name)
    book_url = url.format(b)
    if not book_url.startswith("https"):
        book_url = "https://www.douban.com" + book_url
    try:
        res = requests.get(book_url, headers=headers, proxies=ip[0], timeout=10)
    except:
        res = requests.get(book_url, headers=headers, timeout=10)
    # while True:
    #     try:
    #         res = requests.get(book_url, headers=headers, proxies=ip[0], verify=False,timeout=10)
    #         if res.status_code==200:
    #             break
    #     except:
    #         num+=1
    #         if num==20:
    #             num=0
    #             ip = get_ip()
    soup = BeautifulSoup(res.text, 'html.parser')
    i = 0
    urllist = []
    for soup3 in soup.find_all('div', class_='title'):
        i += 1
        if i > 1: break
        txt = soup3.select('span')[0].get_text()
        # print(txt)
        if txt == '[书籍]':
            for soup4 in soup3.find_all('a', href=True):
                # print(soup4['href'])
                urllist.append(soup4['href'])
    return (urllist)
