#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 19:58
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : post教务系统.py
import requests

cookies = {
    'route': '3f92a87960d19ec836ca88bbf4a5f198',
    'JSESSIONID': 'P9ob4icjFTSB85W3HzVZqKlwc_9cuHBoVDjHR7XJbg1hsmH5UmoG!-1317799401',
    'insert_cookie': '97324480',
    'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE': 'zh_CN',
}

headers = {
    'Origin': 'http://authserver.hnuahe.edu.cn',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://authserver.hnuahe.edu.cn/authserver/login',
    'Proxy-Connection': 'keep-alive',
}

data = {
  'username': '16160101044',
  'password': '3BCGHdtpm3+6d0bcYtHRgPQR3MXqUeUoZVFsobtkOw9I9EEJANrBSRJzZx65tGuBJL3MUq9Ap2vET42PTj7vnW/8eIZFG5Ij7UxA4CRHkB4=',
  'lt': 'LT-3595562-apzozEUVvwVbVDIDK23cbwflOp0D5d1585310805521-KKuw-cas',
  'dllt': 'userNamePasswordLogin',
  'execution': 'e5s1',
  '_eventId': 'submit',
  'rmShown': '1'
}

response = requests.post('http://authserver.hnuahe.edu.cn/authserver/login', headers=headers, cookies=cookies, data=data)

print(response.text.replace("\xa9",""))