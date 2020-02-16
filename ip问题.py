# import json
# import requests
# def crawl_xdaili():
#     """
#     获取讯代理
#     :return: 代理
#     """
#     url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=62258522ca084c20abccfb1028f6ad7e&orderno=YZ2018626596Oclk48&returnType=2&count=20'
#     html = requests(url)
#     if html:
#         result = json.loads(html)
#         proxies = result.get('RESULT')
#         for proxy in proxies:
#             print(proxy.get('ip'))
#             print(proxy.get('port'))
# # def get_page(url):
# #     r = requests.get(url)
# #     r.encoding = 'utf-8'
# #     return r
#
#     #url = 'http://www.glidedsky.com/level/web/crawler-ip-block-1'
# crawl_xdaili()
#     #get_page(url)

import requests

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = 'H961W4N3AFG138WD'
proxyPass = '39D62229BD72E6C0'

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
url = 'http://icanhazip.com/'
response = requests.get(url, headers=headers, proxies=proxies)
ip = response.text.replace('\n', '')
print(ip)
