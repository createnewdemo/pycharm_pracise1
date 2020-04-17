#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 10:01
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : jd100-30.py
import time

import requests
def jd1():
    cookies = {
    'pin': 'jd_5034468c64479',
    'wskey': 'AAJejzkzAEAboJyQuxs0gOs5iZEoeprtrhyVJH1iJ890LporJZDwKDMi-sXn9hFfNn4Uunj3UCpeh8v4H8HLxv78vp7tmwGf',
    'whwswswws': 'rs++2/dm2BXjDrfKV9ui5mAzpcVjxosZ/XAHSB3IF/DFFqWjS/Df2peFrWor/G+YpfXp5Ayvo7MPhIRr3kFqsVQ==',
    'unionwsws': '{"jmafinger":"rs++2\\/dm2BXjDrfKV9ui5mAzpcVjxosZ\\/XAHSB3IF\\/DFFqWjS\\/Df2peFrWor\\/G+YpfXp5Ayvo7MPhIRr3kFqsVQ==","devicefinger":"eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM\\/rOPYHEFqHDROYB7NT\\/IThew4HE4K4qeYZVfTE\\/oVkhUuwabAk\\/3lIrPxwQBC\\/NhrwMwGItu"}',
}
    headers = {
        'Host': 'api.m.jd.com',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'user-agent': 'JD4iPhone/167151 (iPhone; iOS 13.3.1; Scale/2.00)',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    }

    params = (
        ('functionId', 'newReceiveRvcCoupon'),
    )

    data = 'adid=DAE26E1E-DD1B-41CE-960C-75B54AAC589D&area=7_412_3544_47102&body=%7B%22extend%22%3A%220271DFD6890D3B60ACB8BA8A9E49BEB17FE8E6323A36834B63FE69E95D38088E4C06F9F07A4E394FE174377138130821313C6CD9B11FB07A69B2CFC9484073097F6F0BB8CB0BD3A657CE185ADC703B33CF2C80310280441FB991F115051FBC69%22%2C%22source%22%3A%22couponCenter_app%22%2C%22rcType%22%3A%221%22%2C%22shshshfpb%22%3A%22rs%2B%2B2%5C/dm2BXjDrfKV9ui5mAzpcVjxosZ%5C/XAHSB3IF%5C/DFFqWjS%5C/Df2peFrWor%5C/G%2BYpfXp5Ayvo7MPhIRr3kFqsVQ%3D%3D%22%2C%22pageClickKey%22%3A%22CouponCenter%22%2C%22eid%22%3A%22eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM%5C/rOPYHEFqHDROYB7NT%5C/IThew4HE4K4qeYZVfTE%5C/oVkhUuwabAk%5C/3lIrPxwQBC%5C/NhrwMwGItu%22%2C%22childActivityUrl%22%3A%22openapp.jdmobile%253a%252f%252fvirtual%253fparams%253d%257b%255c%2522category%255c%2522%253a%255c%2522jump%255c%2522%252c%255c%2522des%255c%2522%253a%255c%2522couponCenter%255c%2522%257d%22%7D&build=167151&client=apple&clientVersion=8.5.6&d_brand=apple&d_model=iPhone11%2C8&eid=eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM/rOPYHEFqHDROYB7NT/IThew4HE4K4qeYZVfTE/oVkhUuwabAk/3lIrPxwQBC/NhrwMwGItu&isBackground=N&joycious=69&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&openudid=e553adf23e1e66c3258825655268b749b69a61f9&osVersion=13.3.1&partner=apple&rfs=0000&scope=01&screen=828%2A1792&sign=d123b5d53f1c11e036edfe76b1af48a7&st=1586311200829&sv=101&uts=0f31TVRjBSsqndu4/jgUPz6uymy50MQJVNkIKQQ2l6NlWPDD79JybhtIMatoJFQBvRpvDPAu2BNBKNVmJgfXGYp68iBYDFMdl%2Bgc/NCp0icOZDRkySGQa7ARsJSCnnbLYWAhmjZHi57P7GqvpqhzfULWjRM7QB9O28zMGtESqo4hWkNpuEPddc8IbP%2BNN4563bcLcVrPS7thSOXYgu00/A%3D%3D&uuid=coW0lj7vbXVin6h7ON%2BtMNFQqYBqMahr&wifiBssid=unknown'

    response = requests.post('https://api.m.jd.com/client.action', headers=headers, params=params, cookies=cookies,data=data)

    print(response.text)
while 1:
    jd1()
    time.sleep(0.4)


