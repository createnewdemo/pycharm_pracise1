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


def jd():
    cookies = {
        'webp': '1; __jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1586354127715; mba_muid=1586354127714754698460; PPRD_P=UUID.1586354127714754698460; sc_width=1920; shshshfpa=f3a847f5-1cb0-5ea7-c768-f298d80020f5-1586354129; shshshfpb=fdLnd26r9KKyJHyXvwHb2sQ%3D%3D; visitkey=61445534198261649; 3AB9D23F7A4B3C9B=JA76JFQALRDUOZIV5NN7W57CHAYD2GOA7EXROFFQISZNWTPWORPJAOOCFJYNLCLXMZPCB3I6J2ZQ4Q7QYHIXF4NHVA; wxa_level=1; __jda=122270672.1586354127714754698460.1586354127.1586354127.1586524675.2; __jdc=122270672; TrackerID=srOUDoDKIJYjO8w7QsZ-MCyOSOJDHPsTrBzXQXfWPS5ehXKNEiZD77RqT7wocsZvKq13D2yJCQ-HGGmJWQpG5duNq6fxm54io6r9prpAU_v-Bii3lfVG1vthWm1snLEE; pt_key=AAJekHJoADDHYpAKBWcM5LmVr18ZJxESND_bkJOOsjCaMuNdjHeLIdGgfsFrgwajVdpZTqpBwhA; pt_pin=musego; pt_token=vxhg7z1q; pwdt_id=musego; retina=1; cid=9; shshshfp=325b75f47e27339e4ac1524fbf5ceb9e; wqmnx1=MDEyNjM2MGgvLmNKaGNzYWZ5bWkxNDF6NWlBZCAwaVhBZTUgTGVvby43TSBpMzNmZjI1VkVJVShS; __jdb=122270672.4.1586354127714754698460|2.1586524675; mba_sid=15865246754563628231534759851.4; __wga=1586524809948.1586524779762.1586354128420.1586354128420.2.2; shshshsID=8afc72a87f81c169970f277ed4782015_3_1586524810186'}

    # print(j)
    headers = {
        'Host': 's.m.jd.com',
        'accept': '*/*',
        'user-agent': 'jdapp;iPhone;8.5.6;13.3.1;e553adf23e1e66c3258825655268b749b69a61f9;network/wifi;ADID/DAE26E1E-DD1B-41CE-960C-75B54AAC589D;supportApplePay/2;hasUPPay/0;pushNoticeIsOpen/0;model/iPhone11,8;addressid/138416252;hasOCPay/0;appBuild/167151;supportBestPay/0;jdSupportDarkMode/0;pv/216.77;apprpd/ProductCoupon_MergeMain;ref/;psq/0;ads/;psn/e553adf23e1e66c3258825655268b749b69a61f9|420;jdv/0|1586253983;adk/;app_device/IOS;pap/JA2015_311210|8.5.6|IOS 13.3.1;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1',
        'accept-language': 'zh-cn',
        'referer': 'https://coupon.m.jd.com/coupons/show.action?key=72d4354de6d64e18aee92d828a80bc36&roleId=29374352&to=https%3A%2F%2Fcoupon.m.jd.com%2Fcoupons%2Fshow.action%3Fkey%3D72d4354de6d64e18aee92d828a80bc36%26roleId%3D29374352&lng=115.443472&lat=31.977828&sid=f4b521826b86cb9df8b5a479529e700w&un_area=7_412_3544_47102',
    }

    params = (
        ('key', '72d4354de6d64e18aee92d828a80bc36'),
        ('roleId', '29374352'),
        ('linkKey', ''),
        ('to', 'https://coupon.m.jd.com/coupons/show.action?key=72d4354de6d64e18aee92d828a80bc36&roleId=29374352'),
        ('verifycode', ''),
        ('verifysession', ''),
        ('_', '1586254126438'),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKL'),
        ('g_ty', 'ls'),
    )
    # proxies = crawl_xdaili()
    response = requests.get('https://s.m.jd.com/activemcenter/mfreecoupon/getcoupon', headers=headers, params=params,
                            cookies=cookies)
    r = response.text
    try:
        m = re.findall(r'"couponid":(.+),"errmsg":"(.+)",', r)
        print(m[0], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    except:
        print(response.text)


import time
import datetime


def main():
    while 1:
        jd()


if __name__ == '__main__':
    main()
