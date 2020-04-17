#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 11:07
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo1.py
import requests
import json
import requests
import re
def jd():
    cookies ={'shshshfpa': 'c571820e-9c16-b0b6-1b57-c56f75a0933d-1539094005; shshshfpb=1d66d9125a15b4e5da107c3f92e62b707463e76af503f062d5bbcb5f7c; 3AB9D23F7A4B3C9B=2WZYTPYH7AOAQ2QOYFXSDSQ3ZNIGCNMLI2NTVRCRHPA3LDVYODD4XGYIBA6UQ3YIKDJLVUU5MWPCQPJENEJKKTBWJE; unpl=V2_ZzNtbUVSQBMgCUdQLBFaA2JWRQoRVkRCJQ1GXX0aWwxkBEBaclRCFnQUR1FnGV0UZAMZWEBcRhxFCEdkeB5fA2AFEFlBZxBFLV0CFi9JH1c%2bbRdZQVZLFX0MQ1B7KWwGZzMSXHJXQBdzAE5Seh5sNWAzIm1HVUsUcjhHZHopHlE7BRNUQVNAWHULRFJzEVoEYDMTbUE%3d; CCC_SE=ADC_91emn6gwBKOUbjOIieScwP4zX2hRGIQz0n%2fxmp2PTtY%2fUJvNJNXeoTB3%2fbSlZ5J6XK3yHutzB8Oc13%2fqDEW2Am5ccYCKXMhWS8BV49GGg%2fCg9KWUXIb77dy5XyQicE9p1sCtKFnIK9uEEYhgdZy%2fuxwi5OQid5cFfOhnxvZ045o5ND807O4Qf4zjBKcaNGktocV4mkK8cK3GS1VdZSTiaU55oEFGgSuDT1pi78HjwFj2NqahNvmIlHprJugQB%2bqk%2bGptLIqxkxMaWLLZ5KEUD6BkUp1ocIKOAW4kz53ZIzw6NUIQn2M53qpbN1MUIV4DzcYSdFLFaUAyzyr44sCJT7m0xLrJtbaWThWJfxFSdeWSm4j%2ff1x3bMJjjDmnJpeDhBcFrydxyJaminuJjRVKQWVCy%2bR%2fim82xdDCE1zbCl%2bPTJlMRBPoNAStFkzXq24%2bAccXyyKUTAgOkZQFB%2bvK0Buhrs7El5wUY1taX1pBEvE%3d; __jda=122270672.123799706.1586526227.1586526227.1586526229.1; __jdc=122270672; __jdu=123799706; areaId=2; ipLoc-djd=2-2824-0-0; wxa_level=1; retina=0; webp=1; __jdv=122270672%7Cbaidu-search%7Ct_262767352_baidusearch%7Ccpc%7C45209195451_0_6427d005f9774dffb06fa418726826c6%7C1586526235460; mba_muid=123799706; autoOpenApp_downCloseDate_auto=1586526236210_21600000; visitkey=23187129858291741; TrackerID=folVLiW1Zz2nZzOia_3VsIhBKYnRuBY3X2RKQi5K8sMxoev7KTKU7gBNzdh8JR2UaPTkJbVusLuHWLgRz5tc5xYBcsrUciIImCUcyJV1D4i5Hmx9vlZ-ZecuycdZ8GF6; pt_key=AAJekHgpADCU3O_N7WTToKQbn9cd12QPzoL39Vbc1XmNeQwC-fRueAmGn0HoEajtg5YkXbsaxZI; pt_pin=%E4%B8%8B%E4%B8%AA%E8%B7%AF%E5%8F%A3%E4%B8%8B; pt_token=n7lifizw; pwdt_id=%E4%B8%8B%E4%B8%AA%E8%B7%AF%E5%8F%A3%E4%B8%8B; PPRD_P=UUID.123799706; sc_width=1536; shshshfp=ddce03db1ee7ce1ea383210c8f2bd08e; cid=3; wq_area=2_2824_0%7C2; __wga=1586526746521.1586526250170.1586526250170.1586526250170.6.1; shshshsID=3672ca37317f54274e1deb7b3e008277_7_1586526746904; wqmnx1=MDEyNjM3MGgvLm9lb250Mzg0bChzLjYpVzUoIGVoMDdhMzVZZi00WUQjKEg%3D; __jdb=122270672.15.123799706|1.1586526229; mba_sid=1586526235462241148049356798.14'}
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
