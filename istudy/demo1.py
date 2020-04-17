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

import time
import datetime
import requests
import json
import requests
import re
import threading
def jd3(i=3):
    cookies = {
    'pt_key': 'app_openAAJejzk0ADAVQ5t3H9E3lsmpGzMn1L4TW7T0bPR_WAA2gRgLoMhTu5HsCxfnRvSei_8QjHlMVUo',
    'pt_pin': 'jd_5034468c64479',
    'pwdt_id': 'jd_5034468c64479',
    'sid': 'fd7b2ec564e821ba0f5a7b05f9664fbw',
    'unpl': 'V2_ZzNtbRECShcmD04Hck4PBmIDFVoSXkURJlwSXSsfCAJuBBYKclRCFnQUR1FnGVwUZgoZXUdcQxNFOEZVehhdDG8KGl9yZ3MWdThHZHsdVQJjBBdcRlBGEnQNRVx%252bEVsDZDMiXUpRcxF2DkFRfhps0s6txNHkg%252fq%252forrEZHopXTVnAxNZSlBAEXMKdhYVQglrYgQTCBUFFEB8W0BcKVRcAW4EFlpHVkcScA9HUXgRWQ1gBRFtQ2dA%7CADC_HqXm5nGa6x3xW1HvcLoT%2BE2yWHRgofdi6tADvRowGQYzkliz2KLGFnqoj8crrpVmWSQfr2ppRPyiy8ri38XGMw4hRtMS5Fb0eBOaWAttkp979jiGDD25jmAB4TMXVh8hPa2iT8EPzZAsJ70m41RUBDg1rRrkxPpaRd8ChvdPXX7uImaCtnZHmRQeQLbmcPH4L93%2FQ3aG6ZbcUjzM%2BnjH2JaHSUS9k%2Fgy%2BYtVOrOkT0gY7MSrdhu7Xn3b6wh445ep51DyHnoabG56nO%2BT%2B6njhn4t%2Ft4LOOpi24oP3mdPrpPxiMT2vEik0Gh81PVTHo%2BmO8KMDOF1NlG%2FZINaXrNlFU4cM65mOMeU2NJ%2FLzkpWYA3I3a5FEz7%2BEDqo3JgeMrs4nO3lzePneJF%2Bs6vS3lpOtHEkhDPqNjqHC2Yup%2FeUxmT5j2mK4qdOUG0GdLM3XkeFsvwvvlZF8bZHW5eFU2yMwum3bza%2BYg3UkpiATWgpf0Rk8ZOFR%2FBCWNjuh%2FMnJDuc0AzPdF9AENbMMyYR9VcvQaOo7MsV0JwXBSBKYc9aBN%2Fa2aXThUrmCW10%2BF%2FpnArSd%2BbUXAt5IWGMysM4x5uqNYf7qVWSyj%2FyK4BWO3Bz32rHwxLO5KDXSi%2FxYOJXCE%2BjFQhc6WADWB77OX9CuwjqmFNLAGyn5kl51mM0oGkvD2YZv%2FL%2FUaTjTsFm5FUkRId',
    'mba_muid': '15864445934281994656492.246.1586561359560',
    '__jda': '122270672.15864445934281994656492.1586444593.1586533123.1586561354.11',
    '__jdv': '122270672%7Ckong%7Ct_1000089893_%7Ctuiguang%7C053dba6a4b9548178b40d4c579173ce1%7C1586561274000',
    'shshshfpa': '9bc163ec-99d7-3db8-69cc-c2d0c8540755-1586447839',
    'shshshfpb': 'rz2y3Fls5jGdjr7wrLms5Iw%3D%3D',
    '3AB9D23F7A4B3C9B': 'CMWD4GH4AFZRFD5LVUEYQIGCWUMOVP553IVP45HJJG6ZHLOFPE4IT24H27XL45SIOAZX6X67TNMFWL7LOYVKFQZG3Y',
    'BATQW722QTLYVCRD': '{"tk":"jdd01JAVSVRMXDIF3ML5FGQOY4RGNACKUOA4JD4VSPQ6LBHCO76E4GCAEHOZYVI7XA4BMLBR5D65S3CGE5PYOEIQZQUV3PSFPV73HMVA7PGI01234567","t":1586533162065}',
    'shshshfp': '59a439eaf7a5ada2f6f8ed44dfe09117',
    'PPRD_P': 'UUID.15864445934281994656492-LOGID.1586529362536.1050585807',
    'qd_fs': '1586529270586',
    'qd_ls': '1586529270586',
    'qd_sq': '1',
    'qd_ts': '1586529270586',
    'qd_uid': 'K8UAKBWB-P5KKGVWQ2VKIVCM9NTTZ',
    'qd_ad': '-%7C-%7C-%7C-%7C0',
    'mobilev': 'touch',
    '__wga': '1586498628203.1586498311286.1586447838806.1586447838806.2.2',
    'cid': '8',
    'retina': '1',
    'wxa_level': '1',
    'sc_width': '414',
    'visitkey': '20668354492821410',
    'webp': '0',
}
    headers = {'accept': '*/*',
              'referer': 'https://wq.jd.com/activeapi/obtainjdshopfreecouponv2',
              'Content-Type': 'application/x-www-form-urlencoded',
              'accept-language': 'zh-cn',
              'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)'}

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
    response = requests.get('https://s.m.jd.com/activemcenter/mfreecoupon/getcoupon', headers=headers,
                            params=params,
                            cookies=cookies)
    r = response.text
    print(r)
    # try:
    #     m = re.findall(r'"couponid":(.+),"errmsg":"(.+)",', r)
    #     print(m[0], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),'===========线程%d=========='%i)
    # except:
    #     print('====================恭喜中奖=====================','===========线程%d=========='%i)
    #     print(response.text,'===========线程%d=========='%i)
while 1:
    jd3()
    time.sleep(1)

