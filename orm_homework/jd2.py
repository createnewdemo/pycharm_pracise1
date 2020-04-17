#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:10
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : jd7折.py
import requests


def jd():
    cookies = {'wxa_level': '1', ' webp': '1',
               ' __jda': '122270672.15863253608761993172972.1586325360.1586325360.1586325360.1',
               ' __jdv': '122270672%7Cdirect%7C-%7Cnone%7C-%7C1586325360876', ' __jdc': '122270672',
               ' mba_muid': '15863253608761993172972', ' visitkey': '61488995368789872',
               ' autoOpenApp_downCloseDate_auto': '1586325361408_21600000',
               ' shshshfpa': 'e86b04d4-7436-d7f5-400c-ffed96fdb102-1586325376',
               ' 3AB9D23F7A4B3C9B': 'RQ35NTYHLK73WBZL5NEI7QVIYSV7PRWVQDL65O3ZZUJDYO7IGCDFW3UWYJWXS4T6BIMNUD4GTH6UOLU7YVXZ5ZPQU4',
               ' jcap_dvzw_fp': 'f749fd2fce2e800f59b360ee0a32c8d8$715893833564', ' whwswswws': '',
               ' TrackerID': '8R6-qZggbnEovS77xNarXCoSjNuZVJe90sr_0CV8ttf7WmJOuq3-nPfT6D_cmyEwPzLCvUKtX2t4-3UVwo8va85grz8P8KHFqPrZxCcrGljUdAnwxazocwbivoAFw10Z',
               ' pt_key': 'AAJejWfKADDEr-Rks--8WQAe-g7bBEfGHbUvAPmhbm7JDDkUn4MI4XI9SKMcsfPOR8hT3mmPk5M',
               ' pt_pin': 'TTQ19970625', ' pt_token': 'a8ka558h', ' pwdt_id': 'TTQ19970625', ' retina': '1',
               ' PPRD_P': 'UUID.15863253608761993172972', ' shshshfp': 'b23929e6d319480ebd0203696a15faf5',
               ' sc_width': '360', ' shshshfpb': 'zwhEb0%2FnRvo%20RKyBCoNN9sw%3D%3D', ' cid': '3',
               ' __wga': '1586325470908.1586325459794.1586325459794.1586325459794.2.1', ' wq_area': '7_549_3119%7C1',
               ' shshshsID': '81c381823876239cf51b943098cf6b1c_3_1586325471198',
               ' wqmnx1': 'MDEyNjM3NTpvLnVoaT00ZTIwbzkmcEZwZEZzd24lMzZlYSVJM2wuJi4mYmJmOTByMV8wOTh6LnVyMDlpMnBpM01lKWUzMWVpNnI0YTRWVUhGSA%3D%3D',
               ' __jdb': '122270672.5.15863253608761993172972|1.1586325360',
               ' mba_sid': '15863253608777658091065139092.5'}

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


while 1:
    jd()
