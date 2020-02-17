import requests
from lxml import etree
import time

import requests

# url = 'http://icanhazip.com/'
# response = requests.get(url,headers=headers,proxies=proxies)
# ip = response.text.replace('\n','')
# print(ip)
c = 0
for x in range(1, 1001):

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
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://www.glidedsky.com/level/web/crawler-ip-block-1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }

    url1 = 'http://icanhazip.com/'
    response = requests.get(url1, headers=headers, proxies=proxies)
    ip = response.text.replace('\n', '')
    print(ip)

    url = 'http://www.glidedsky.com/level/web/crawler-ip-block-1?page={}'.format(x)

    print(url)
    # print(url)
    r = requests.get(url=url, headers=headers, proxies=proxies)
    # print(proxies)
    print(r.status_code)
    r.encoding = 'utf-8'
    print(r.text)
    html = etree.HTML(r.text)
    shu = html.xpath("//div[@class='col-md-1']/text()")
    print(shu)
    print("正在算第%d页" % x)
    for m in shu:
        i = m.strip()
        a = int(i)
        # print(a)
        c += a
        break
    break
    print("第%d页的和%d" % (x, c))
print(c)
