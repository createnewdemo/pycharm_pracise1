# import requests
# from lxml import etree
# import time
from requests import request
#
cookies = {
    '_ga': 'GA1.2.950415565.1581756506',
    '_gid': 'GA1.2.395578867.1581756507',
    'footprints': 'eyJpdiI6ImV4dG5TUFBjSlRISkY1YnJyMHVNTkE9PSIsInZhbHVlIjoiMm5LS1wvTDhyQWtqQnhDZEk3UGF0aTVrbm1VWStRTVBqRFRvM1FsTkxxcFJhWWliWlJLMVBnVVJERU9iOWhzNVwvIiwibWFjIjoiOGI1NWYzYjg4MDA2YTgxYzFjYjgwMGZiMzgzNzdiODZiOTgxZmQ3OTdkYmZkOGE0Y2UyMDE5MDM0NjFlM2M1YiJ9',
    'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1581756506,1581756608,1581765671',
    'Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1581773628',
    'XSRF-TOKEN': 'eyJpdiI6IlZ2bVwvSG5pTWErdXBhNmdVbHMwWStRPT0iLCJ2YWx1ZSI6Ik5UWHhvVGZyeUJaYXl2Vzh1alJESHFmWCtjTEZreEpVWENwVzgxUHpRdnFnOFVOVGxhVEVremhQXC9YREJwYnd2IiwibWFjIjoiYzRiNjg1OTAxYTQwZWQ1ZjNiYzU1MGM1YTFiZjMxNjg1ZWM2MjM0MWZlZTQ4Y2VmZDA1MjZhOTQ3YmQzYzM3YyJ9',
    'glidedsky_session': 'eyJpdiI6ImI3bDU0djNIMnZZVEoxNFBycHJicEE9PSIsInZhbHVlIjoiQ0FEOEZqMjM3MU1cL2R6dGJyMDMzaFdnVldpMVdCcFZESVdEbVJJK1NtMER6NTU3WTVud3BkRlpOSFp0aUxjR1YiLCJtYWMiOiIwMDY5NTY1ODZjODA4NTliMTIxMDc0NDFmMzljN2NiY2M1M2QwZjJjMDUzOTJhNzIwZTBhZWNiNGJjNzhjZmIyIn0%3D',
}

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
#
# # 代理服务器
#
# proxyHost = "http-dyn.abuyun.com"
# proxyPort = "9020"
#
# # 代理隧道验证信息
# proxyUser = 'H961W4N3AFG138WD'
# proxyPass = '39D62229BD72E6C0'
#
# proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
#     "host": proxyHost,
#     "port": proxyPort,
#     "user": proxyUser,
#     "pass": proxyPass,
# }
#
# proxies = {
#     "http": proxyMeta,
#     "https": proxyMeta,
# }
#
# c = 0
# for x in range(1, 1001):

#     url1 = 'http://icanhazip.com/'
#     response = requests.get(url1, headers=headers, proxies=proxies)
#     ip = response.text.replace('\n', '')
#     print(ip)
#     url = 'http://www.glidedsky.com/level/web/crawler-ip-block-{}'.format(x)
#     r = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
#     print(url)
#     # print(r.status_code)
#     r.encoding = 'utf-8'
#     # print(r.text)
#     time.sleep(1)
#
#     html = etree.HTML(r.text)
#     shu = html.xpath("//div[@class='col-md-1']/text()")
#     # print(shu)
#     print("正在算第%d页" % x)
#     for m in shu:
#         i = m.strip()
#         a = int(i)
#         print(a)
#         c += a
#         # break
#     # break
#     print("第%d页的和%d" % (x, c))
# print(c)



"""

下面是官方文档

"""

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

if __name__ == '__main__':
    crawl_xdaili()