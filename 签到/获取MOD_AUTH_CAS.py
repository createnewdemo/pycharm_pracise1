#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 17:03
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 获取MOD_AUTH_CAS.py
import requests
headers = {
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://authserver.hnuahe.edu.cn/authserver/login?service=https^%^3A^%^2F^%^2Fhnuahe.cpdaily.com^%^2Fportal^%^2Flogin',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
params = (
    ('username', '16160101043^'),
    ('pwdEncrypt2', 'pwdEncryptSalt^'),
    ('v', '09781242791953622'),
)

response = requests.get('http://authserver.hnuahe.edu.cn/authserver/login?service=https%3A%2F%2Fhnuahe.cpdaily.com%2Fportal%2Flogin', headers=headers, params=params, verify=False)

print(response.status_code)
print(response.text)