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
        '__jdu': '1640513903; shshshfpa=a86be0b6-b916-40ba-35c5-70640184844c-1565103916; shshshfpb=tHODioKdwYpVeiraQm27%208g%3D%3D; user-key=ea8bab28-5b72-4ac6-92a1-e22abf1bb6ad; areaId=7; ipLoc-djd=7-549-3119-0; PCSYCityID=CN_410000_411500_411524; pinId=yGrKhqZyHfKsuwx5kdThNrV9-x-f3wj7; pin=jd_5034468c64479; _tp=MIA%2F6%2FADlgFQNV0O76wPSv4bAgCk7B%2FiaxNWTRxU%2Fgo%3D; _pst=jd_5034468c64479; cn=140; TrackID=1ykeLEhQICdaO-vWcVCTNzYFkeeXI1GFgNok913WoJ48h8Dh5eexPM1gMggQXx1zS4madydhVl40Fx4x5WqMBaIn-N2774kWQ8H432h7z58w; unick=DemoLi1; unpl=V2_ZzNtbUpVQRZ0C0ABeh0OBGJTGlxKU0ARdgoRAXkfVA00AxNZclRCFnQUR1FnGFQUZwMZXkJcQxJFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseWQRjAxBVQ1VzJXI4dmR4EVoEYAIiXHJWc1chVEZUeBlYACoDFVhDU0MXfQlEZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9332027d05c04a90952523fd3799b105|1586402477314; __jdc=122270672; wlfstk_smdl=kcxaij85b4enkoawcvnauv0yud20v6eg; wxa_level=1; webp=1; mba_muid=1640513903; visitkey=61589042337060043; retina=1; PPRD_P=UUID.1640513903; sc_width=360; __jda=122270672.1640513903.1565103905.1586402477.1586411524.16; __wga=1586411846769.1586411524587.1586402533128.1586402533128.5.2; cid=3; wqmnx1=MDEyNjM5NTpvOTBsaXIgIFhsNUhlQy44IDMzNDJLRUYoJQ%3D%3D; __jdb=122270672.9.1640513903|16.1586411524; mba_sid=15864115243436513310331849869.9; shshshfp=135954adb4efd4304eb5683a755e8663; shshshsID=fb925f1eb6523020fcaedd682153bd75_7_1586411851302; 3AB9D23F7A4B3C9B=PW4YUOEJI2DQWR53SXIVQYG6V6ZWVO4C5YJZAEO5PHI4JNOV2IEODP74WGGCXFDCJSO47HNNVVOP7QC7DLP6MIKSNM; TrackerID=zzR7-kE9IQZ0yGN4E01OF1TFVnGFnlUuzE8XBvHuyiQ53o1zYk49mVTdI9jHi34xuHWpkidY_k5V3THPA6fWHHk2K3aLh09O5PDeSqLFVgJrIHBxgWne8rvTQQ0G5DqMScRJQGg_53lr0Z5HOFqEPQ; pt_key=AAJejrlZADAPBFtZNFfw0FD_6GDef5AFPbztvZr4fzzdD2lcq_4n-COY9zrplNGz2fiTLWtNcp4; pt_pin=jd_5034468c64479; pt_token=qsf99lvu; pwdt_id=jd_5034468c64479; __jd_ref_cls=MLoginRegister_LoginSuccess'}
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

    print(r, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


import time
import datetime


def main():
    while 1:
        jd()


if __name__ == '__main__':
    main()
