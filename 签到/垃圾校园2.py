#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:56
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 垃圾校园2.py
import requests
import json
import requests
def get():
    import requests

    cookies = {
        'clientType': 'cpdaily_student',
        'sessionToken': '206a0c75-d270-4b1a-9422-68f20a3cf736',
        'tenantId': 'hnuahe',
        'MOD_AUTH_CAS': 'ST-225151-M03bGBeYaOq3N6dOlRCI1585283285485-70EW-cas',
        'acw_tc': '76b20ff115844991465806596e13bd2d4eef36fd0afe08f0b309725075008f',
    }

    headers = {
        'Host': 'hnuahe.cpdaily.com',
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/json',
        'Origin': 'https://hnuahe.cpdaily.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5386791424)cpdaily/8.1.12  wisedu/8.1.12',
        'Referer': 'https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/mobile/index.html?signWid=143467&signInstanceWid=6811',
    }

    data = '{"wid":"6811","content":"143467"}'

    response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/getUnSeenQuestion',
                             headers=headers, cookies=cookies, data=data)


cookies = {
    'clientType': 'cpdaily_student',
    'sessionToken': '206a0c75-d270-4b1a-9422-68f20a3cf736',
    'tenantId': 'hnuahe',
    'MOD_AUTH_CAS': 'ST-225151-M03bGBeYaOq3N6dOlRCI1585283285485-70EW-cas',
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

response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-sign-apps/stu/sign/detailSignInstance', headers=headers, cookies=cookies, data=data)
print(response.text)