#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:10
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : jd7折.py
import requests
import json
import requests
def crawl_xdaili():
    """
    获取讯代理
    :return: 代理
    """
    url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=d26050ff9c3a495b8256b7b7b7920782&orderno=YZ2018626596Oclk48&returnType=2&count=1'
    r = requests.get(url)
    if r:
        result = json.loads(r.text)
        proxies = result.get('RESULT')
        print(proxies)
        for proxy in proxies:
            print(proxy.get('ip'))
            print(proxy.get('port'))
            proxies = {
                'http':'http://' + proxy.get('ip') + ":"+ proxy.get('port')
            }
            print(proxies)
            return proxies
def get_page():
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }
    proxies = crawl_xdaili()
    r = requests.get('http://icanhazip.com/')
    r.encoding = 'utf-8'
    response = requests.get('http://icanhazip.com/', headers=headers, proxies=proxies, timeout=5)
    ip = response.text.replace('\n', '')
    return ip
import re
def jd():
    cookies = {
        'mba_muid': '1586433088782807759544.235.1586443971678',
        'mba_sid': '235.2',
        '__jda': '122270672.1586433088782807759544.1586433088.1586441146.1586443970.5',
        '__jdb': '122270672.1.1586433088782807759544|5.1586443970',
        '__jdv': '122270672%7Ckong%7Ct_1000089893_%7Ctuiguang%7C3fd6c202df5242f2b6ff39db4aebed68%7C1586441142000',
        'unpl': 'V2_ZzNtbUAAFhInC0dXLk5YBmIARV4RUBRCdwATB35JCFYzVhVUclRCFnQUR1FnGFQUZAAZXEZcRhZFOEZVehhdDG8KGl9yZ3MWdThHZHsdVQJiBhJdR1dFHHQLRlF9HFUHYDMiXUpRcxV2CkFVeRts0s6txNHkg%252fq%252forrEZHopXTVnAxNZSlBAEXMKdgIVGV0EZgITXUtQR1h1DE9TfhxcBWIDFFRDVEMQcw1PVnwpXTVk%7CADC_HqXm5nGa6x3xW1HvcLoT%2BE2yWHRgofdi6tADvRowGQYzkliz2KLGFnqoj8crrpVmWSQfr2ppRPyiy8ri38XGMw4hRtMS5Fb0eBOaWAttkp979jiGDD25jmAB4TMXVh8hPa2iT8EPzZAsJ70m41RUBDg1rRrkxPpaRd8ChvdPXX7uImaCtnZHmRQeQLbmcPH4L93%2FQ3aG6ZbcUjzM%2BnjH2JaHSUS9k%2Fgy%2BYtVOrOkT0gY7MSrdhu7Xn3b6wh445ep51DyHnoabG56nO%2BT%2B6njhn4t%2Ft4LOOpi24oP3mdPrpPxiMT2vEik0Gh81PVTHo%2BmO8KMDOF1NlG%2FZINaXrNlFU4cM65mOMeU2NJ%2FLzkpWYA3I3a5FEz7%2BEDqo3JgeMrs4nO3lzePneJF%2Bs6vS3lpOtHEkhDPqNjqHC2Yup%2FeUxmT5j2mK4qdOUG0GdLM3XkeFsvwvvlZF8bZHW5eFU2yMwum3bza%2BYg3UkpiATWgpf0Rk8ZOFR%2FBCWNjuh%2FMnJDuc0AzPdF9AENbMMyYR9VcvQaOo7MsV0JwXBSBKYc9aBN%2Fa2aXThUrmCW10%2BF%2FpnArSd%2BbUXAt5IWGMysM4x5uqNYf7qVWSyj%2FyK4BWO3Bz32rHwxLO5KDXSi%2FxYOJXCE%2BjFQhc6WADWB77OX9CuwjqmFNLAGyn5kl51mM0oGkvD2YZv%2FL%2FUaTjTsFm5FUkRId',
        'pt_key': 'app_openAAJejwxOADBRIMID3vT4057aLlJtJ3YQ3AtvXuUuM4DjDLc8PA3iEV0WeL6GgslKUYk1fDmG-Io',
        'pt_pin': 'jd_5034468c64479',
        'pwdt_id': 'jd_5034468c64479',
        'sid': '77bbe3d88b7426c397605ff757c0437w',
        'shshshfpa': '4fbcd3fd-a465-86fe-7895-49320e95259a-1586357768',
        'shshshfpb': 'rz2y3Fls5jGdjr7wrLms5Iw%3D%3D',
        '3AB9D23F7A4B3C9B': 'CMWD4GH4AFZRFD5LVUEYQIGCWUMOVP553IVP45HJJG6ZHLOFPE4IT24H27XL45SIOAZX6X67TNMFWL7LOYVKFQZG3Y',
        'PPRD_P': 'LOGID.1586441310810.1335897456',
        'shshshfp': 'e5281c8d9556b15433209e6248ae9ea3',
        'BATQW722QTLYVCRD': '{"tk":"jdd01VRJAGJQJL6WRUWEMXSU6BOVOI6R6GHYDLABV3YAH544ENQTOD2PNK2T7FJ5JY254FE7F54Q2FNVXPEVBXFBX7PH4Q6XVI4DKA36FAGI01234567","t":1586441158501}',
        'visitkey': '61396627416802081',
    }

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
    #proxies = crawl_xdaili()
    response = requests.get('https://s.m.jd.com/activemcenter/mfreecoupon/getcoupon', headers=headers, params=params, cookies=cookies)
    r=response.text
    try:

        m = re.findall(r'"couponid":(.+),"errmsg":"(.+)",',r)
        print(m[0])
    except:
        print("恭喜您已经抢到7折优惠券，快到券包里看看吧。")

import time
while 1:
    jd()



# 开始抢券
# scheduled_time = "2017-10-29 14:38"
# def getCoupon():
#     print('等待抢券中......')
#     while (True):
#         # 当前时间
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
#
#         # 如果到预定时间就开始发送请求，然后打印结果
#         if now == scheduled_time:
#             r = session.get(couponUrl)
#             print(r.text)
#             break
