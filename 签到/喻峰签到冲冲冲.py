#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 15:44
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 喻峰签到冲冲冲.py
import datetime
import json
import threading
import time
import requests
import schedule


def get():
    cookies = {
        'clientType': 'cpdaily_student',
        'sessionToken': 'a531947b-712a-4c2b-a03c-259c63df2573',
        'tenantId': 'hnuahe',
        'MOD_AUTH_CAS': 'ST-2015418-so4sgFQZzngSzXcZM3NY1585311284722-CZOn-cas',
        'acw_tc': '76b20fe515853112846622077e234b39fd8b9bd7bc4db10bd0e3d5738ddd46',
    }

    headers = {
        'Host': 'hnuahe.cpdaily.com',
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/json',
        'Origin': 'https://hnuahe.cpdaily.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4421002752)cpdaily/8.1.12  wisedu/8.1.12',
        'Referer': 'https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/mobile/index.html?signWid=143467&signInstanceWid=6908',
    }
    data = '{"signInstanceWid":"7008","signWid":"143467"}'
    response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/detailSignInstance',
                             headers=headers, cookies=cookies, data=data)
    r = response.content
    r = json.loads(r)  # 传进去的是 JSON 数据 返回的是一个字典
    todaycode = r["datas"]["signInstanceWid"]
    #print(r)
    print(todaycode)
    return todaycode
def post():
    cookies = {
        'clientType': 'cpdaily_student',
        'sessionToken': '',
        'tenantId': 'hnuahe',
        'MOD_AUTH_CAS': 'ST-2015418-so4sgFQZzngSzXcZM3NY1583112745-CZOn-cas',
        'acw_tc': '',
    }
    headers = {
        'Host': 'hnuahe.cpdaily.com',
        'Content-Type': 'application/json',
        'Cpdaily-Extension': '7Q881vmOiX52ZMMaeIbU2lVKKB2Y2n/yeCgeJmxRk4DDPqL97WnLcwKjBQ1k Gv/6EJKDvK3qW0bQ2JU8b3sNeXGLD4vBn9ZU98qmcvqXRegcBwICAb8mSWGA 0z649TpWlsqgHrzrWHm9r1NdlQ+1EPUK+RvnP7nckhrdlpR9NvxZjXJfEeIw HLczkphOB0u+gtnsiFx4S9uOB179VLCE+n/btQ1b6aJAAeyOPF8l7D7uOG0w V8HeFeV72hQcdzsbyopNVH9Plu7L5tRxOW4QoOTyIv7nwBGj',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
    }
    todaycode = get()
    data = {
        "signInstanceWid": todaycode,
        "longitude": 113.75937959333567,
        "latitude": 34.771712551287045,
        "isMalposition": 1,
        "abnormalReason": "正常",
        "signPhotoUrl": "",
        "position": "中国河南省信阳市固始县"
    }
    #https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/getQAconfigration
    #https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/detailSignInstance
    response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/submitSign', headers=headers, cookies=cookies, data=json.dumps(data))
    #print(response.content)
    con = response.text
    con.encode('utf-8').decode('unicode_escape')
    print(con)
schedule.every().day.at("20:38").do(post)
# while True:
#      schedule.run_pending()
#      time.sleep(1)
