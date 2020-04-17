#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 11:28
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 时间格式带毫秒.py
import datetime
import time

import requests
#
# print(datetime.datetime.now())  # 2019-01-28 11:09:01.529864
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))  # 2019-01-28 11:09:01.529864
# print(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))  # 20190128110901529864
# 获取京东时间
def get_time():
    res = requests.get(
        url='https://a.jd.com//ajax/queryServerData.html',
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'})
    data_server = res.json()
    # return data_server['serverTime']
    print(data_server['serverTime'])
    print(time.time())
get_time()