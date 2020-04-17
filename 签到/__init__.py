#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:47
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : __init__.py.py
import datetime
import threading


def func():
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # print(now_time,next_time,next_year,next_month,next_day)
    # 获取明天7点时间
    next_time = datetime.datetime.strptime(
        str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 08:01:00", "%Y-%m-%d %H:%M:%S")
    # 获取距离明天7点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)
    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    #timer = threading.Timer(timer_start_time, )
    #timer.start()
func()