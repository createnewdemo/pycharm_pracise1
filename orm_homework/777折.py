#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:10
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : jd7折.py
import requests


def jd():
    cookies = {'__jdu': '1640513903', ' shshshfpa': 'a86be0b6-b916-40ba-35c5-70640184844c-1565103916',
               ' shshshfpb': 'tHODioKdwYpVeiraQm27%208g%3D%3D', ' user-key': 'ea8bab28-5b72-4ac6-92a1-e22abf1bb6ad',
               ' areaId': '7', ' ipLoc-djd': '7-549-3119-0', ' PCSYCityID': 'CN_410000_411500_411524',
               ' unpl': 'V2_ZzNtbRcDF0J2XUYALExfBWJQRl0RVkESdl0VXHweX1djUxtaclRCFnQUR1FnGFUUZwIZWUBcRxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseWQRjAxBVQ1VzJXI4dmR5GFoNZwMiXHJWc1chVEZWcxhdBCoDFVhDU0MXfQlEZHopXw%3d%3d',
               ' TrackID': '1yaWfEky2U2frIOs1SNXURxw8OFXwYV24DduDrR3gaS6MK5vxk5ERJHrFfliJQGybPmBm-kBF2ry-8TtcXaTtH3RP5SXB9jFT78cHkg-XB3M',
               ' thor': '242FAD7E41A6E62A66F3ED85D1CE160B7A9A2389194DFBE96566222DEFA842BA565E5A8FF9047AAC5C9CC36834F85146D92182F40FA50B3D7A9E587EA621C91A859F108798C76CCC1EB73D747CCED8E72027FDABDB615EA806D1CFEFC2E0EE6232C19E5C47985821A7B0C43E3FCA4AC2E7528F69C2C3A58E2E93F501E3D392159149EC01E2DAAC91C92D642FCCA8F29C2D4618D2B62EA83E8FF3F3D48D7DEDA5',
               ' pinId': 'yGrKhqZyHfKsuwx5kdThNrV9-x-f3wj7', ' pin': 'jd_5034468c64479', ' unick': 'jd_171901clg',
               ' ceshi3.com': '201', ' _tp': 'MIA%2F6%2FADlgFQNV0O76wPSv4bAgCk7B%2FiaxNWTRxU%2Fgo%3D',
               ' _pst': 'jd_5034468c64479', ' cn': '140',
               ' __jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_deef2d1efd214be1b0362db9662c5a86|1586314464403',
               ' __jda': '122270672.1640513903.1565103905.1586313418.1586314434.12', ' __jdc': '122270672',
               ' wxa_level': '1', ' retina': '1', ' webp': '1', ' mba_muid': '1640513903',
               ' visitkey': '61604435499761128', ' PPRD_P': 'UUID.1640513903', ' sc_width': '360',
               ' 3AB9D23F7A4B3C9B': 'PW4YUOEJI2DQWR53SXIVQYG6V6ZWVO4C5YJZAEO5PHI4JNOV2IEODP74WGGCXFDCJSO47HNNVVOP7QC7DLP6MIKSNM',
               ' TrackerID': 'VLjDWm2hPT_k8Kj9gOmiRiAbiNanOH6iLFFurB8qYPg_IGenMpHlyuJbcfnCl-G97bb0Le1_YHDDIwPmvfxTWTO7Unk-CeXHEJNnN-6_vNIHphoHEn0EA1fx0NfJYdqbbbSkC1s5kAFsROcQrcOpEw',
               ' pt_key': 'AAJejUOAADBCFqRANTT7ClNCTE9c73jspNjMMwc1P_Jwbxj1aS7ixMkpJW4CgCNlq_FjqRVFFCw',
               ' pt_pin': 'jd_5034468c64479', ' pt_token': 'ydkyacbp', ' pwdt_id': 'jd_5034468c64479',
               ' shshshfp': 'b23929e6d319480ebd0203696a15faf5', ' cid': '3', ' wq_area': '7_549_3119%7C1',
               ' shshshsID': '1d5efed8b0855f02409d284e2be3a400_14_1586316328409',
               ' wqmnx1': 'MDEyNjM2MXQvbi5lZ3B0dDYzNm8vTCBpOzl1UiBXLzZNa2tyNTIgZXIuMllhLTQxUlMjISk%3D',
               ' __jdb': '122270672.30.1640513903|12.1586314434', ' mba_sid': '15863147285152381578587956630.20',
               ' __jd_ref_cls': 'MDownLoadFloat_TopNewExpo',
               ' __wga': '1586316525746.1586314787119.1586314787119.1586314787119.7.1'}
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

    response = requests.get('https://s.m.jd.com/activemcenter/mfreecoupon/getcoupon', headers=headers, params=params,
                            cookies=cookies)

    print(response.text)


# while 1:
#     jd()
jd()

"""

headers = {
    'pragma': 'no-cache',
    'cookie': '__jdu=1640513903; shshshfpa=a86be0b6-b916-40ba-35c5-70640184844c-1565103916; shshshfpb=tHODioKdwYpVeiraQm27%208g%3D%3D; user-key=ea8bab28-5b72-4ac6-92a1-e22abf1bb6ad; areaId=7; ipLoc-djd=7-549-3119-0; PCSYCityID=CN_410000_411500_411524; unpl=V2_ZzNtbRcDF0J2XUYALExfBWJQRl0RVkESdl0VXHweX1djUxtaclRCFnQUR1FnGFUUZwIZWUBcRxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseWQRjAxBVQ1VzJXI4dmR5GFoNZwMiXHJWc1chVEZWcxhdBCoDFVhDU0MXfQlEZHopXw%3d%3d; TrackID=1yaWfEky2U2frIOs1SNXURxw8OFXwYV24DduDrR3gaS6MK5vxk5ERJHrFfliJQGybPmBm-kBF2ry-8TtcXaTtH3RP5SXB9jFT78cHkg-XB3M; thor=242FAD7E41A6E62A66F3ED85D1CE160B7A9A2389194DFBE96566222DEFA842BA565E5A8FF9047AAC5C9CC36834F85146D92182F40FA50B3D7A9E587EA621C91A859F108798C76CCC1EB73D747CCED8E72027FDABDB615EA806D1CFEFC2E0EE6232C19E5C47985821A7B0C43E3FCA4AC2E7528F69C2C3A58E2E93F501E3D392159149EC01E2DAAC91C92D642FCCA8F29C2D4618D2B62EA83E8FF3F3D48D7DEDA5; pinId=yGrKhqZyHfKsuwx5kdThNrV9-x-f3wj7; pin=jd_5034468c64479; unick=jd_171901clg; ceshi3.com=201; _tp=MIA%2F6%2FADlgFQNV0O76wPSv4bAgCk7B%2FiaxNWTRxU%2Fgo%3D; _pst=jd_5034468c64479; cn=140; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_deef2d1efd214be1b0362db9662c5a86|1586314464403; __jda=122270672.1640513903.1565103905.1586313418.1586314434.12; __jdc=122270672; wxa_level=1; retina=1; webp=1; mba_muid=1640513903; visitkey=61604435499761128; autoOpenApp_downCloseDate_auto=1586314729030_21600000; jcap_dvzw_fp=f749fd2fce2e800f59b360ee0a32c8d8$715787548155; whwswswws=; PPRD_P=UUID.1640513903; sc_width=360; 3AB9D23F7A4B3C9B=PW4YUOEJI2DQWR53SXIVQYG6V6ZWVO4C5YJZAEO5PHI4JNOV2IEODP74WGGCXFDCJSO47HNNVVOP7QC7DLP6MIKSNM; TrackerID=VLjDWm2hPT_k8Kj9gOmiRiAbiNanOH6iLFFurB8qYPg_IGenMpHlyuJbcfnCl-G97bb0Le1_YHDDIwPmvfxTWTO7Unk-CeXHEJNnN-6_vNIHphoHEn0EA1fx0NfJYdqbbbSkC1s5kAFsROcQrcOpEw; pt_key=AAJejUOAADBCFqRANTT7ClNCTE9c73jspNjMMwc1P_Jwbxj1aS7ixMkpJW4CgCNlq_FjqRVFFCw; pt_pin=jd_5034468c64479; pt_token=ydkyacbp; pwdt_id=jd_5034468c64479; shshshfp=b23929e6d319480ebd0203696a15faf5; cid=3; wqmnx1=MDEyNjM4MGhjLmNlQ2MxOU01dW8gUExBSzNMR2guMWxpMXNmNDJFSCZS; __jdb=122270672.28.1640513903|12.1586314434; mba_sid=15863147285152381578587956630.18; __wga=1586316326852.1586314787119.1586314787119.1586314787119.6.1; wq_area=7_549_3119%7C1; shshshsID=1d5efed8b0855f02409d284e2be3a400_14_1586316328409; __jd_ref_cls=MProductCoupon_Specialcoupon',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 's.m.jd.com',
    'referer': 'https://coupon.m.jd.com/center/getCouponCenter.action',
}

params = (
    ('coupon', '1D43EBC21040BCAEAF7FA8F48DB36267,2C05732EAD93FBC7C6755C8356B735F016A40FD5257221746B71B57A576451E750AC93F8FAD90D456227C60734534054'),
    ('batchid', '302368966'),
    ('_', '1586316341976'),
    ('sceneval', '2'),
    ('g_login_type', '1'),
    ('callback', 'jsonpCBKA'),
    ('g_ty', 'ls'),
)

response = requests.get('https://s.m.jd.com/activemcenter/mcouponcenter/receivecoupon', headers=headers, params=params, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://s.m.jd.com/activemcenter/mcouponcenter/receivecoupon?coupon=1D43EBC21040BCAEAF7FA8F48DB36267%2C2C05732EAD93FBC7C6755C8356B735F016A40FD5257221746B71B57A576451E750AC93F8FAD90D456227C60734534054&batchid=302368966&_=1586316341976&sceneval=2&g_login_type=1&callback=jsonpCBKA&g_ty=ls', headers=headers, verify=False)
"""
