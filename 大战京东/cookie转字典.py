#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 11:11
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : cookie转字典.py
import json

data = ''
with open('ck.txt', 'r') as f:
    f = f.read()
    cookie = {}
    for line in f.split(';'):
        key, value = line.split('=', 1)
        cookie[key] = value
json = json.dumps(cookie)
print(json)

