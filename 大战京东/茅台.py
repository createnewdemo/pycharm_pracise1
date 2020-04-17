#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 10:04
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 茅台.py
import requests
import json
def jdmt():

    cookies = {
        'seckillSid': '',
        'seckillSku': '100012043978',
        '3AB9D23F7A4B3C9B': 'CMWD4GH4AFZRFD5LVUEYQIGCWUMOVP553IVP45HJJG6ZHLOFPE4IT24H27XL45SIOAZX6X67TNMFWL7LOYVKFQZG3Y',
        '__tak': 'b115ccf117d974fdb397f99b4901ab8b1ea2504b9a37537243753413e70d22585f7b90c8a7129769c1cf437dfabe4542bf07679caa0a5750be3623c7a9491f3b1f653d83d17a95e79ba9c481154b868e',
        'unpl': 'V2_ZzNtbUYFShRyAURQKBsPUWJXEV4RBEIWIABEUn8ZC1A0VBMOclRCFnQUR1FnGV0UZgsZX0BcQBZFOEZVehhdDG8KGl9yZ3MWdThHZHsdVQJiChFfSl9CEHILRlF9HFUHYDMiXUpRcxV0CUdVexlYAmAEFm2V%252fu3D%252ba6S7dHO7odXAiJccldDFHEAQVd%252fH141MW0SXENWQhR1AUFQNhlYDGAGG15AX0sUcA9FVH4fWQxlBCJcclQ%253d%7CADC_HqXm5nGa6x3xW1HvcLoT%2BE2yWHRgofdi6tADvRowGQYzkliz2KLGFnqoj8crrpVmWSQfr2ppRPyiy8ri38XGMw4hRtMS5Fb0eBOaWAttkp979jiGDD25jmAB4TMXVh8hPa2iT8EPzZAsJ70m41RUBDg1rRrkxPpaRd8ChvdPXX7uImaCtnZHmRQeQLbmcPH4L93%2FQ3aG6ZbcUjzM%2BnjH2JaHSUS9k%2Fgy%2BYtVOrOkT0gY7MSrdhu7Xn3b6wh445ep51DyHnoabG56nO%2BT%2B6njhn4t%2Ft4LOOpi24oP3mdPrpPxiMT2vEik0Gh81PVTHo%2BmO8KMDOF1NlG%2FZINaXrNlFU4cM65mOMeU2NJ%2FLzkpWYA3I3a5FEz7%2BEDqo3JgeMrs4nO3lzePneJF%2Bs6vS3lpOtHEkhDPqNjqHC2Yup%2FeUxmT5j2mK4qdOUG0GdLM3XkeFsvwvvlZF8bZHW5eFU2yMwum3bza%2BYg3UkpiATWgpf0Rk8ZOFR%2FBCWNjuh%2FMnJDuc0AzPdF9AENbMMyYR9VcvQaOo7MsV0JwXBSBKYc9aBN%2Fa2aXThUrmCW10%2BF%2FpnArSd%2BbUXAt5IWGMysM4x5uqNYf7qVWSyj%2FyK4BWO3Bz32rHwxLO5KDXSi%2FxYOJXCE%2BjFQhc6WADWB77OX9CuwjqmFNLAGyn5kl51mM0oGkvD2YZv%2FL%2FUaTjTsFm5FUkRId',
        'mid': 'ZSYxApA-FHqks9o1FclgjrRzQW-uc-7hlgMPUKraFMc',
        'seckill100012043978': 'gyZYvtOu17zqGdko3zvkx1Q25UlyGb9NGPpehhjFPUtVnjeKvjzlW1gq6CrsqFit0W36PY7QgBh6oQlik1RrgQ9gfBeHFfK1muaVFiqX7b8oEZPWJhN0Mrwjg+Gak1/p83olgpa/S9ak4k72v/jj+xncR+BughkNXHdwww/RgpL5Py3FeisL1t9XBViXLh22ia2BCOqW3QjuK910',
        'pt_key': 'app_openAAJejzk0ADAVQ5t3H9E3lsmpGzMn1L4TW7T0bPR_WAA2gRgLoMhTu5HsCxfnRvSei_8QjHlMVUo',
        'pt_pin': 'jd_5034468c64479',
        'pwdt_id': 'jd_5034468c64479',
        'sid': 'fd7b2ec564e821ba0f5a7b05f9664fbw',
        'shshshfpb': 'rz2y3Fls5jGdjr7wrLms5Iw%3D%3D',
        '__jd_ref_cls': 'Mnpm_ComponentApplied',
        'mba_muid': '15864445934281994656492.237.1586483950789',
        'mba_sid': '237.73',
        'shshshfp': '7be5983935b3cbd48d2e38f331a297e5',
        'shshshfpa': '9bc163ec-99d7-3db8-69cc-c2d0c8540755-1586447839',
        'shshshsID': '4f1b37d96dba63a7d04d6be6a6b5f982_4_1586483950475',
        '__jda': '122270672.15864445934281994656492.1586444593.1586447793.1586482476.3',
        '__jdb': '122270672.7.15864445934281994656492|3.1586482476',
        '__jdc': '122270672',
        '__jdv': '122270672%7Ckong%7Ct_1000089893_%7Ctuiguang%7C5c806835b3be4e22bb02d93751fdbf0b%7C1586482402000',
        'pre_seq': '37',
        'pre_session': 'e553adf23e1e66c3258825655268b749b69a61f9|586',
        'plusCustomBuryPointToken': '1586483944871_4020',
        'BATQW722QTLYVCRD': '{"tk":"jdd01O7MTV2E2BMFCAWWATR5MTLNVOVTIQ3NZJWSZJUWBY6IP3EO746UW2WIUYRMNH4KPEE7MTLGJSQTUHWNZYPT2DGJV5FFHIZUP5H5NXRQ01234567","t":1586483803916}',
        'PPRD_P': 'UUID.15864445934281994656492-LOGID.1586482476733.135133249',
        '__wga': '1586448125613.1586447838806.1586447838806.1586447838806.2.1',
        'cid': '8',
        'retina': '1',
        'wxa_level': '1',
        'sc_width': '414',
        'visitkey': '20668354492821410',
        'webp': '0',
    }

    headers = {
        'Host': 'marathon.jd.com',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://marathon.jd.com',
        'accept-language': 'zh-cn',
        'user-agent': 'jdapp;iPhone;8.5.6;13.3.1;e553adf23e1e66c3258825655268b749b69a61f9;network/wifi;ADID/DAE26E1E-DD1B-41CE-960C-75B54AAC589D;supportApplePay/2;hasUPPay/0;pushNoticeIsOpen/0;model/iPhone11,8;addressid/138416252;hasOCPay/0;appBuild/167151;supportBestPay/0;jdSupportDarkMode/0;pv/237.76;apprpd/Productdetail_MainPage;ref/WareInfoViewController;psq/41;ads/;psn/e553adf23e1e66c3258825655268b749b69a61f9|586;jdv/0|kong|t_1000089893_|tuiguang|5c806835b3be4e22bb02d93751fdbf0b|1586482402;adk/;app_device/IOS;pap/JA2015_311210|8.5.6|IOS 13.3.1;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1',
        'referer': 'https://marathon.jd.com/seckillM/seckill.action?skuId=100012043978&num=1&rid=1586484003',
    }

    params = (
        ('skuId', '100012043978'),
    )

    data = 'num=2&addressId=495332106&yuShou=true&isModifyAddress=true&name=%E6%9D%8E%E4%B8%96%E6%9E%97&provinceId=7&cityId=549&countyId=3119&townId=34605&addressDetail=%E6%B2%B3%E5%8D%97%E4%BF%A1%E9%98%B3%E5%B8%82%E5%95%86%E5%9F%8E%E5%8E%BF%E4%B8%8A%E7%9F%B3%E6%A1%A5%E9%95%87%E8%80%81%E8%8F%9C%E5%B8%82%E5%9C%BA%E6%97%81%E8%BE%B9&mobile=171%2A%2A%2A%2A9811&mobileKey=a8e585a13e2542680fb88829c37571fe&email=&invoiceTitle=4&invoiceCompanyName=&invoiceContent=1&invoiceTaxpayerNO=&invoiceEmail=&invoicePhone=171%2A%2A%2A%2A9811&invoicePhoneKey=a8e585a13e2542680fb88829c37571fe&invoice=true&password=&codTimeType=3&paymentType=4&overseas=0&phone=&areaCode=&token=d55378e023af64a35d55b11221038242'

    response = requests.post('https://marathon.jd.com/seckillnew/orderService/submitOrder.action', headers=headers, params=params, cookies=cookies, data=data)
    print(response.text)

while 1:
    jdmt()


