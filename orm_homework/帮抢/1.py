#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 21:43
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 1.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:10
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : jd7折.py
import requests


def jd():
    cookies = {
        'mba_muid': '1586444394193184654963.235.1586444482892',
        'mba_sid': '235.50',
        '__jda': '122270672.1586444394193184654963.1586444394.1586444394.1586444394.1',
        '__jdb': '122270672.2.1586444394193184654963|1.1586444394',
        '__jdv': '122270672%7Ckong%7Ct_1000089893_%7Ctuiguang%7C3fd6c202df5242f2b6ff39db4aebed68%7C1586441142000',
        'pt_key': 'app_openAAJejzjAADBDofd_Cy07-JtOz6KX4sx4nzg0Ei2FFSIx7UIJwdvgKxF9JYOYzLKy0kdx4zFpdes',
        'pt_pin': 'jd_JahGxmtPmGvW',
        'pwdt_id': 'jd_JahGxmtPmGvW',
        'sid': '38bd5f3529b2d1de8f3917b60deb4b5w',
        'unpl': 'V2_ZzNtbUAAFhInC0dXLk5YBmIARV4RUBRCdwATB35JCFYzVhVUclRCFnQUR1FnGFQUZAAZXEZcRhZFOEZVehhdDG8KGl9yZ3MWdThHZHsdVQJiBhJdR1dFHHQLRlF9HFUHYDMiXUpRcxV2CkFVeRts0s6txNHkg%252fq%252forrEZHopXTVnAxNZSlBAEXMKdgIVGV0EZgITXUtQR1h1DE9TfhxcBWIDFFRDVEMQcw1PVnwpXTVk%7CADC_HqXm5nGa6x3xW1HvcLoT%2BE2yWHRgofdi6tADvRowGQYzkliz2KLGFnqoj8crrpVmWSQfr2ppRPyiy8ri38XGMw4hRtMS5Fb0eBOaWAttkp979jiGDD25jmAB4TMXVh8hPa2iT8EPzZAsJ70m41RUBDg1rRrkxPpaRd8ChvdPXX7uImaCtnZHmRQeQLbmcPH4L93%2FQ3aG6ZbcUjzM%2BnjH2JaHSUS9k%2Fgy%2BYtVOrOkT0gY7MSrdhu7Xn3b6wh445ep51DyHnoabG56nO%2BT%2B6njhn4t%2Ft4LOOpi24oP3mdPrpPxiMT2vEik0Gh81PVTHo%2BmO8KMDOF1NlG%2FZINaXrNlFU4cM65mOMeU2NJ%2FLzkpWYA3I3a5FEz7%2BEDqo3JgeMrs4nO3lzePneJF%2Bs6vS3lpOtHEkhDPqNjqHC2Yup%2FeUxmT5j2mK4qdOUG0GdLM3XkeFsvwvvlZF8bZHW5eFU2yMwum3bza%2BYg3UkpiATWgpf0Rk8ZOFR%2FBCWNjuh%2FMnJDuc0AzPdF9AENbMMyYR9VcvQaOo7MsV0JwXBSBKYc9aBN%2Fa2aXThUrmCW10%2BF%2FpnArSd%2BbUXAt5IWGMysM4x5uqNYf7qVWSyj%2FyK4BWO3Bz32rHwxLO5KDXSi%2FxYOJXCE%2BjFQhc6WADWB77OX9CuwjqmFNLAGyn5kl51mM0oGkvD2YZv%2FL%2FUaTjTsFm5FUkRId',
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

    response = requests.get('https://s.m.jd.com/activemcenter/mfreecoupon/getcoupon', headers=headers, params=params,
                            cookies=cookies)

    print(response.text)


while 1:
    jd()
