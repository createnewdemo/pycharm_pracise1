#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 23:14
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 多线程jd.py

import re
import time
import datetime
import json
import threading
import requests

ck = [ {
        'webp': '1; __jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1586354127715; mba_muid=1586354127714754698460; PPRD_P=UUID.1586354127714754698460; sc_width=1920; shshshfpa=f3a847f5-1cb0-5ea7-c768-f298d80020f5-1586354129; shshshfpb=fdLnd26r9KKyJHyXvwHb2sQ%3D%3D; visitkey=61445534198261649; 3AB9D23F7A4B3C9B=JA76JFQALRDUOZIV5NN7W57CHAYD2GOA7EXROFFQISZNWTPWORPJAOOCFJYNLCLXMZPCB3I6J2ZQ4Q7QYHIXF4NHVA; wxa_level=1; __jda=122270672.1586354127714754698460.1586354127.1586354127.1586524675.2; __jdc=122270672; TrackerID=srOUDoDKIJYjO8w7QsZ-MCyOSOJDHPsTrBzXQXfWPS5ehXKNEiZD77RqT7wocsZvKq13D2yJCQ-HGGmJWQpG5duNq6fxm54io6r9prpAU_v-Bii3lfVG1vthWm1snLEE; pt_key=AAJekHJoADDHYpAKBWcM5LmVr18ZJxESND_bkJOOsjCaMuNdjHeLIdGgfsFrgwajVdpZTqpBwhA; pt_pin=musego; pt_token=vxhg7z1q; pwdt_id=musego; retina=1; cid=9; shshshfp=325b75f47e27339e4ac1524fbf5ceb9e; wqmnx1=MDEyNjM2MGgvLmNKaGNzYWZ5bWkxNDF6NWlBZCAwaVhBZTUgTGVvby43TSBpMzNmZjI1VkVJVShS; __jdb=122270672.4.1586354127714754698460|2.1586524675; mba_sid=15865246754563628231534759851.4; __wga=1586524809948.1586524779762.1586354128420.1586354128420.2.2; shshshsID=8afc72a87f81c169970f277ed4782015_3_1586524810186'},

{'__jdu': '1640513903; shshshfpa=a86be0b6-b916-40ba-35c5-70640184844c-1565103916; shshshfpb=tHODioKdwYpVeiraQm27%208g%3D%3D; user-key=ea8bab28-5b72-4ac6-92a1-e22abf1bb6ad; areaId=7; ipLoc-djd=7-549-3119-0; PCSYCityID=CN_410000_411500_411524; pinId=yGrKhqZyHfKsuwx5kdThNrV9-x-f3wj7; pin=jd_5034468c64479; _tp=MIA%2F6%2FADlgFQNV0O76wPSv4bAgCk7B%2FiaxNWTRxU%2Fgo%3D; _pst=jd_5034468c64479; cn=140; jcap_dvzw_fp=f749fd2fce2e800f59b360ee0a32c8d8$715787548155; whwswswws=; TrackID=1ykeLEhQICdaO-vWcVCTNzYFkeeXI1GFgNok913WoJ48h8Dh5eexPM1gMggQXx1zS4madydhVl40Fx4x5WqMBaIn-N2774kWQ8H432h7z58w; unick=DemoLi1; unpl=V2_ZzNtbUpVQRZ0C0ABeh0OBGJTGlxKU0ARdgoRAXkfVA00AxNZclRCFnQUR1FnGFQUZwMZXkJcQxJFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseWQRjAxBVQ1VzJXI4dmR4EVoEYAIiXHJWc1chVEZUeBlYACoDFVhDU0MXfQlEZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9332027d05c04a90952523fd3799b105|1586402477314; webp=1; mba_muid=1640513903; visitkey=61589042337060043; PPRD_P=UUID.1640513903; sc_width=360; 3AB9D23F7A4B3C9B=PW4YUOEJI2DQWR53SXIVQYG6V6ZWVO4C5YJZAEO5PHI4JNOV2IEODP74WGGCXFDCJSO47HNNVVOP7QC7DLP6MIKSNM; __jdc=122270672; wxa_level=1; __jda=122270672.1640513903.1565103905.1586486064.1586509849.18; autoOpenApp_downCloseDate_auto=1586509849981_21600000; retina=1; TrackerID=JLF0lWpTq_xn_tPUQTdt539JNs2rHg_Iz2YbYva5sGozVj2jarztdXDkBqlOOB8V2ZC5tcUYvwGNxZUd9NOLYLrrCNAhediipZx4IgNTqOfBwmS_blDvtpDMbBz_ONse6YmVOZ2sAV2fe-KTSZSWlw; pt_key=AAJekDjYADBRu38GSu4NaPf9Q84mwd8BoxEldXRsC1LoxUXrZc3lGgXcs6sgfjBUM4BkX2R2FRI; pt_pin=jd_567a79f85f94b; pt_token=7zylppmv; pwdt_id=jd_567a79f85f94b; cid=9; shshshfp=b23929e6d319480ebd0203696a15faf5; wqmnx1=MDEyNjM2M3BxYy9ueGw9MWNsMTIwejVpQWQgMGlYQWU1IExlb28uNU0gaTMzZmYyNVZFSVUoUg%3D%3D; __wga=1586510087836.1586509852624.1586411524587.1586402533128.4.3; shshshsID=5bb9ebee7c789a0e480f2b9bf2d8f932_5_1586510088036; __jdb=122270672.8.1640513903|18.1586509849; mba_sid=15865098496087664013632996427.8; __jd_ref_cls=MCommonHead_Back'},
]
#
# 获取京东时间
def get_time():
    res = requests.get(
        url='https://a.jd.com//ajax/queryServerData.html',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'})
    data_server = res.json()
    return data_server['serverTime']
def run(ck,count):
    cookies = ck

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
        print(m[0], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),'线程%s'%count)
    except:
        print('====================恭喜中奖=====================')
        print(response.text)


def main():
    n = 0
    while n < 4:
        n += 1
        num = 0
        for i in ck:
            run(i,num)
        t_obj = []
        num1= 0
        for i in ck:
            num1 += 1
            t = threading.Thread(target=run, args=(i,num1))
            t_obj.append(t)
            t.start()
        for t in t_obj:
            t.join()
main()
