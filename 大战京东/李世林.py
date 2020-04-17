#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 11:07
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo1.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:10
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : jd7折.py
import requests
import json
import requests
import re
import time
import datetime

def jd():
    cookies = {"block_call_jdapp": "11", " __jdc": "122270672", " pt_token": "aw4ynobc",
               " shshshfp": "518570ff611c8fc64b861df47b7f196b",
               " wqmnx1": "MDEyNjM5OGguL2FldT02djQ0aShOVzRlLkxlbzNTNy8xWVU0V1NIKQ%3D%3D",
               " visitkey": "20413199096444176", " cid": "9",
               " __jda": "122270672.15866099081031425722690.1586609908.1586609908.1586609908.1", " wxa_level": "1",
               " sc_width": "1920", " webp": "1", " retina": "0", " mba_sid": "1586609908106800551315319548.2",
               " shshshfpb": "vtuZfZLBtKUd3IpU8xR7DLQ%3D%3D", " pt_pin": "jd_5034468c64479",
               " pwdt_id": "jd_5034468c64479", " __wga": "1586609938630.1586609899056.1586609899056.1586609899056.2.1",
               " shshshsID": "4e6701793201efafc4965e3ae5f26d98_3_1586609939100",
               " shshshfpa": "93296639-88b0-23a6-2101-b0738f90247e-1586609899",
               " __jdv": "122270672%7Cdirect%7C-%7Cnone%7C-%7C1586609899061", " mba_muid": "15866099081031425722690",
               " __jdb": "122270672.2.15866099081031425722690|1.1586609908",
               " PPRD_P": "CT.138631.36.4-UUID.15866099081031425722690",
               " pt_key": "AAJekb8PADBBQvBuPNUighZvg-vMeDZnXG3Drxv1KXauXFPC6eiDMGM1MqPiVdxsfL3b0aa4ozw",
               " TrackerID": "QVQ8yRbOTVjTqQyShp4CGhyUROzUSsCh3CIqE0_SNLE3mvzQEc42_iIBLdf8uDIQn6_DiLC8fPDED3xGg89T4dvW7lHsc_lRLTOXYJYbmvVFJg1yOnKzb-dlGMQ7v7G5",
               " __jd_ref_cls": "MCommonBottom_Home", " whwswswws": "",
               " jcap_dvzw_fp": "da34e48eec0ad7c745f78d68c40ebe95$718739157296"}
    # print(j)
    headers = {
        'Host': 's.m.jd.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'referer': 'https://coupon.m.jd.com/coupons/show.action?key=72d4354de6d64e18aee92d828a80bc36&roleId=29374352&to=https%3A%2F%2Fcoupon.m.jd.com%2Fcoupons%2Fshow.action%3Fkey%3D72d4354de6d64e18aee92d828a80bc36%26roleId%3D29374352&lng=115.443472&lat=31.977828&sid=f4b521826b86cb9df8b5a479529e700w&un_area=7_412_3544_47102',
    }

    params = (
        ('key', '72d4354de6d64e18aee92d828a80bc36'),
        ('roleId', '29374352'),
        ('to', 'https://coupon.m.jd.com/coupons/show.action?key=72d4354de6d64e18aee92d828a80bc36&roleId=29374352'),
    )

    response = requests.get('https://s.m.jd.com/activemcenter/mfreecoupon/getcoupon', headers=headers, params=params,
                            cookies=cookies)
    r = response.text
    #print(r,file=open("output.txt", "a"))
    print(response.text)
    # try:
    #     m = re.findall(r'"couponid":(.+),"errmsg":"(.+)",', r)
    #     # print(m[0], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),file=open("output.txt", "a"))
    #     print(m[0], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    # except:
    #     print('====================恭喜中奖=====================')
    #     # print(response.text,file=open("output.txt", "a"))
    #     print(response.text)


# # 获取京东时间
# def get_time():
#     res = requests.get(
#         url='https://a.jd.com//ajax/queryServerData.html',
#         headers={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'})
#     data_server = res.json()
#     print(data_server['serverTime'])
#     return data_server['serverTime']
#
# # 把时间戳转换成格式化
# def timestamp_to_str(timestamp=None, format='%Y-%m-%d %H:%M:%S.%f'):
#     if timestamp:
#         time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
#         result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
#         return result
#     else:
#         return time.strptime(format)

# print(s,type(s))
# print(timestamp_to_str(1586612926348))
# 转换为指定的格式
# timeStamp = s
# timeArray = time.localtime(s)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S.%f'", timeArray)
# print(otherStyleTime)

def main():
    while 1:
        jd()
if __name__ == '__main__':
    main()

