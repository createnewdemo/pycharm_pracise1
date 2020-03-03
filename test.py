# -*- coding: gbk -*-
import json
import requests


def crawl_xdaili():
    """
    获取讯代理
    :return: 代理
    """
    url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=62258522ca084c20abccfb1028f6ad7e&orderno=YZ2018626596Oclk48&returnType=2&count=1'
    r = requests.get(url)
    if r:
        result = json.loads(r.text)
        proxies = result.get('RESULT')
        for proxy in proxies:
            # print(proxy.get('ip'))
            # print(proxy.get('port'))
            proxies = {
                'http': 'http://' + proxy.get('ip') + ":" + proxy.get('port'),
                'https': 'https://' + proxy.get('ip') + ":" + proxy.get('port')

            }
            print(proxies)
            return proxies


cookies = {
    'ASP.NET_SessionId': 'uicdf2ltejpuriu2o0toaxw0',
    'Hm_lvt_83853859c7247c5b03b527894622d3fa': '1582460741,1582466325,1582631385',
    'security_session_verify': '6aeb3884e3755a4f23a27d1cdb40ceef',
    'security_session_mid_verify': 'f17bdf2e9756bd02e77621aba6d6258a',
    'Hm_lpvt_83853859c7247c5b03b527894622d3fa': '1582637344',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.landchina.com/default.aspx?tabid=261&ComName=default&security_verify_data=313932302c31303830',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

params = (
    ('tabid', '261'),
    ('ComName', 'default'),
)
proxies = crawl_xdaili()

response = requests.get('https://www.landchina.com/default.aspx?tabid=261&ComName=default', headers=headers,
                        params=params, cookies=cookies, proxies=proxies, timeout=10)
print(response.status_code)
