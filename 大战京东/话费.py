#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 20:03
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 话费.py
import requests
def jdhf():
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

    headers = {
        'Host': 'api.m.jd.com',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'user-agent': 'jdapp;iPhone;8.5.6;13.3.1;e553adf23e1e66c3258825655268b749b69a61f9;network/4g;ADID/DAE26E1E-DD1B-41CE-960C-75B54AAC589D;JDEbook/openapp.jdreader;supportApplePay/2;hasUPPay/0;pushNoticeIsOpen/0;model/iPhone11,8;addressid/-2074359180;hasOCPay/0;appBuild/167151;supportBestPay/0;jdSupportDarkMode/0;pv/252.62;apprpd/ProductCoupon_MergeMain;ref/;psq/0;ads/;psn/e553adf23e1e66c3258825655268b749b69a61f9|700;jdv/0|1586605880;adk/;app_device/IOS;pap/JA2015_311210|8.5.6|IOS 13.3.1',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    }

    params = (
        ('functionId', 'newReceiveRvcCoupon'),
    )

    data = 'adid=DAE26E1E-DD1B-41CE-960C-75B54AAC589D&area=7_549_3119_34605&body=%7B%22extend%22%3A%220271DFD6890D3B60ACB8BA8A9E49BEB17FE8E6323A36834B63FE69E95D38088EB6909FE0E44A0A8D10F61FDFF7081D6C62B138D55F89DE3FA1DEC6759CECCBA1C5ADBA73CC0BF9DD7011D32A3F4A15C9A7B87E9A3E7004B0E793871A278E4AB0%22%2C%22source%22%3A%22couponCenter_app%22%2C%22rcType%22%3A%221%22%2C%22shshshfpb%22%3A%22rs%2B%2B2%5C/dm2BXjDrfKV9ui5mAzpcVjxosZ%5C/XAHSB3IF%5C/DFFqWjS%5C/Df2peFrWor%5C/G%2BYpfXp5Ayvo7MPhIRr3kFqsVQ%3D%3D%22%2C%22pageClickKey%22%3A%22CouponCenter%22%2C%22eid%22%3A%22eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM%5C/rOPYHEFqHDROYB7NT%5C/IThew4HE4K4qeYZVfTE%5C/oVkhUuwabAk%5C/3lIrPxwQBC%5C/NhrwMwGItu%22%2C%22childActivityUrl%22%3A%22openapp.jdmobile%253a%252f%252fvirtual%253fparams%253d%257b%255c%2522category%255c%2522%253a%255c%2522jump%255c%2522%252c%255c%2522des%255c%2522%253a%255c%2522couponCenter%255c%2522%257d%22%7D&build=167151&client=apple&clientVersion=8.5.6&d_brand=apple&d_model=iPhone11%2C8&eid=eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM/rOPYHEFqHDROYB7NT/IThew4HE4K4qeYZVfTE/oVkhUuwabAk/3lIrPxwQBC/NhrwMwGItu&isBackground=N&joycious=87&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&openudid=e553adf23e1e66c3258825655268b749b69a61f9&osVersion=13.3.1&partner=apple&rfs=0000&scope=01&screen=828%2A1792&sign=bd812647241bc01875ff6be02041562b&st=1586606400060&sv=121&uts=0f31TVRjBSsqndu4/jgUPz6uymy50MQJCnoZILfPKo8bjRfx1EBhwPKSvwyve4wlDk65VBRszVz1ZpjzVTQcyKX4yyEdIRpirn3T5%2BHB/zHXPIdkUk7tb7/diaFUNp1sCV1jOwTem0uQvZOJQR9IPYufsVAVyD3t0ho40WrZxAQ9Vkm2onlmS%2BOwjPrx3YJ3GkK16ZBug13Ab3UKsQcrew%3D%3D&uuid=coW0lj7vbXVin6h7ON%2BtMNFQqYBqMahr&wifiBssid=unknown'

    response = requests.post('https://api.m.jd.com/client.action', headers=headers, params=params, cookies=cookies,
                             data=data)

    print(response.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.post('https://api.m.jd.com/client.action?functionId=newReceiveRvcCoupon', headers=headers, cookies=cookies, data=data)
while 1:
    jdhf()