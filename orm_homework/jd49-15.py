import time

import requests
import schedule


def jd():
    cookies = {
        'pin': 'jd_5034468c64479',
        'wskey': 'AAJejZIXAECB1MTlLQWoWuml1j6ClsAEOYyV4n7OaqTYRkW6VmY-L-Cta7_e9eoNcI0iHsi2iFfaIuxjroIfTB6-xT0g2s_q',
        'whwswswws': 'rs++2/dm2BXjDrfKV9ui5mAzpcVjxosZ/XAHSB3IF/DFFqWjS/Df2peFrWor/G+YpfXp5Ayvo7MPhIRr3kFqsVQ==',
        'unionwsws': '{"jmafinger":"rs++2\\/dm2BXjDrfKV9ui5mAzpcVjxosZ\\/XAHSB3IF\\/DFFqWjS\\/Df2peFrWor\\/G+YpfXp5Ayvo7MPhIRr3kFqsVQ==","devicefinger":"eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM\\/rOPYHEFqHDROYB7NT\\/IThew4HE4K4qeYZVfTE\\/oVkhUuwabAk\\/3lIrPxwQBC\\/NhrwMwGItu"}',
    }

    headers = {
        'Host': 'api.m.jd.com',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'user-agent': 'jdapp;iPhone;8.5.6;13.3.1;e553adf23e1e66c3258825655268b749b69a61f9;network/wifi;ADID/DAE26E1E-DD1B-41CE-960C-75B54AAC589D;supportApplePay/2;hasUPPay/0;pushNoticeIsOpen/0;model/iPhone11,8;addressid/138416252;hasOCPay/0;appBuild/167151;supportBestPay/0;jdSupportDarkMode/0;pv/226.10;apprpd/OrderCenter_List;ref/;psq/9;ads/;psn/e553adf23e1e66c3258825655268b749b69a61f9|486;jdv/0|1586328265;adk/;app_device/IOS;pap/JA2015_311210|8.5.6|IOS 13.3.1',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    }

    params = (
        ('functionId', 'newReceiveRvcCoupon'),
    )

    data = 'adid=DAE26E1E-DD1B-41CE-960C-75B54AAC589D&area=7_412_3544_47102&body=%7B%22extend%22%3A%220271DFD6890D3B60ACB8BA8A9E49BEB17FE8E6323A36834B63FE69E95D38088E0F33B73C7FEDFEBD23B1F7DF40D4B68D79459815278F7988110184BD33D0F2B970D6DA67A414F426E906612639D9DF9862F30CE1EE354A8E7D1802ED5B7C2650%22%2C%22source%22%3A%22couponCenter_app%22%2C%22rcType%22%3A%221%22%2C%22shshshfpb%22%3A%22rs%2B%2B2%5C/dm2BXjDrfKV9ui5mAzpcVjxosZ%5C/XAHSB3IF%5C/DFFqWjS%5C/Df2peFrWor%5C/G%2BYpfXp5Ayvo7MPhIRr3kFqsVQ%3D%3D%22%2C%22pageClickKey%22%3A%22CouponCenter%22%2C%22eid%22%3A%22eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM%5C/rOPYHEFqHDROYB7NT%5C/IThew4HE4K4qeYZVfTE%5C/oVkhUuwabAk%5C/3lIrPxwQBC%5C/NhrwMwGItu%22%2C%22childActivityUrl%22%3A%22openapp.jdmobile%253a%252f%252fvirtual%253fparams%253d%257b%255c%2522category%255c%2522%253a%255c%2522jump%255c%2522%252c%255c%2522des%255c%2522%253a%255c%2522couponCenter%255c%2522%257d%22%7D&build=167151&client=apple&clientVersion=8.5.6&d_brand=apple&d_model=iPhone11%2C8&eid=eidIbb96812202s3YNemWeoLQw2T4uokzA400mDXp8MM/rOPYHEFqHDROYB7NT/IThew4HE4K4qeYZVfTE/oVkhUuwabAk/3lIrPxwQBC/NhrwMwGItu&isBackground=N&joycious=69&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&openudid=e553adf23e1e66c3258825655268b749b69a61f9&osVersion=13.3.1&partner=apple&rfs=0000&scope=01&screen=828%2A1792&sign=879b1e9a2ed4abb88e3f96e822078025&st=1586339999391&sv=122&uts=0f31TVRjBSsqndu4/jgUPz6uymy50MQJwxKVvQvFu3dtPpfJCDJAfHx0SPWJiamTXoKu3kdz6Jq/zygD1/6cK6U19YqxStxxbMeyVtTptHoSvI/%2BdLLZDERpAjZjGyvyrSXxnkM3wMr4FMzhpQ5Ubk5nCyAi1P6f2KnUGnpzi9UdrY25GeuzEgMIPuhEsqcMBTLh%2Bw5esQEH1ovMVdK21A%3D%3D&uuid=coW0lj7vbXVin6h7ON%2BtMNFQqYBqMahr&wifiBssid=unknown'

    response = requests.post('https://api.m.jd.com/client.action', headers=headers, params=params, cookies=cookies, data=data)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.post('https://api.m.jd.com/client.action?functionId=newReceiveRvcCoupon', headers=headers, cookies=cookies, data=data)
    print(response.text)
while 1:
    jd()

