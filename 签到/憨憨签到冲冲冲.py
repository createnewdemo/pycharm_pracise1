#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 憨憨签到冲冲冲.py
import datetime
import threading
import requests
import json
import time
import schedule


def get():
    cookies = {
        'clientType': 'cpdaily_student',
        'sessionToken': '206a0c75-d270-4b1a-9422-68f20a3cf736',
        'tenantId': 'hnuahe',
        'MOD_AUTH_CAS': 'HHVnvp7xVhiFG6mXby1aDX1583112745',
        'acw_tc': '76b20ff115844991465806596e13bd2d4eef36fd0afe08f0b309725075008f',
    }

    headers = {
        'Host': 'hnuahe.cpdaily.com',
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/json',
        'Origin': 'https://hnuahe.cpdaily.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5394100224)cpdaily/8.1.12  wisedu/8.1.12',
        'Referer': 'https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/mobile/index.html?signWid=143467&signInstanceWid=6908',
    }

    data = '{"signInstanceWid":"7008","signWid":"143467"}'

    response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/detailSignInstance',
                             headers=headers, cookies=cookies, data=data)
    r = response.content
    r = json.loads(r)# 传进去的是 JSON 数据 返回的是一个字典

    todaycode = r["datas"]["signInstanceWid"]
    #print(r)
    print(todaycode)
    return todaycode

def post():
    cookies = {
        'clientType': 'cpdaily_student',
        'sessionToken': 'fca2819f-a4bd-4688-8be9-e7ae5417efd4',
        'tenantId': 'hnuahe',
        'MOD_AUTH_CAS': 'HHVnvp7xVhiFG6mXby1aDX1583112745',
        'acw_tc': '76b20ff115844991465806596e13bd2d4eef36fd0afe08f0b309725075008f',
    }
    headers = {
        'Host': 'hnuahe.cpdaily.com',
        'Content-Type': 'application/json',
        'Cpdaily-Extension': '7Q881vmOiX52ZMMaeIbU2lVKKB2Y2n/yeCgeJmxRk4DDPqL97WnLcwKjBQ1k Gv/6EJKDvK3qW0bQ2JU8b3sNeXGLD4vBn9ZU98qmcvqXRegcBwICAb8mSWGA 0z649TpWlsqgHrzrWHm9r1NdlQ+1EPUK+RvnP7nckhrdlpR9NvxZjXJfEeIw HLczkphOB0u+gtnsiFx4S9uOB179VLCE+n/btQ1b6aJAAeyOPF8l7D7uOG0w V8HeFeV72hQcdzsbyopNVH9Plu7L5tRxOW4QoOTyIv7nwBGj',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'User-Agent': '%E4%BB%8A%E6%97%A5%E6%A0%A1%E5%9B%AD/1 CFNetwork/1121.2.2 Darwin/19.3.0',
    }
    todaycode = get()
    data = {

        "signInstanceWid": todaycode,
        "longitude": 115.44978534475491,
        "latitude": 31.98412448592618,
        "isMalposition": 1,
        "abnormalReason": "正常",
        "signPhotoUrl": "",
        "position": "河南省信阳市商城县"

    }
    #https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/getQAconfigration
    #https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/detailSignInstance
    response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/submitSign', headers=headers, cookies=cookies, data=json.dumps(data))
    #print(response.content)
    con = response.text
    con.encode('utf-8').decode('unicode_escape')
    print(con)
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
    timer = threading.Timer(timer_start_time,post)
    timer.start()
schedule.every().day.at("20:39").do(post)
# while True:
#      schedule.run_pending()
#      time.sleep(1)
post()