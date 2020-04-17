# -*- coding: gbk -*-
import requests

cookies = {
    'UM_distinctid': '170a9417a21b97-06c091463e1b94-3a614f0b-1fa400-170a9417a2266',
    'PHPSESSID': '0',
    'uerrNum': '0',
    'uerrExpire': '0',
    'healAjax': '0',
    'name': '0',
    'utid': '0',
    'uuid': '0',
    'uin': '0',
    'uvauth': '0',
    'sid': 'fHp3NT84',
    'schoolExt': '53',
    'schoolType': '1',
    'schoolName': '%E6%B2%B3%E5%8D%97%E7%89%A7%E4%B8%9A%E7%BB%8F%E6%B5%8E%E5%AD%A6%E9%99%A2',
    'CNZZDATA1264334274': '0%7C1583387663',
    'type': '1',
    'ulauth': '47c19798bc6c3a0b642f0e325d8d4f44',
    'uniName': '%E5%8C%85%E8%A3%85%E4%B8%8E%E5%8D%B0%E5%88%B7%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2',
}

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://jktb.haedu.gov.cn/?act=login',
    'Connection': 'keep-alive',
}

params = (
    ('act', 'verify'),
)

response = requests.get('http://jktb.haedu.gov.cn/', headers=headers, params=params, cookies=cookies)

print(response.text)
