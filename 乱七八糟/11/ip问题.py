
import requests
import time
def crawl_xdaili():
    """
    获取讯代理
    :return: 代理
    """
    cookies = {
        'JSESSIONID': '1D9F95D546740EFCD8655CF44D02207F',
        'UM_distinctid': '1702451bd537ee-0317685a6e92fd-3a614f0b-1fa400-1702451bd5473c',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=62258522ca084c20abccfb1028f6ad7e&orderno=YZ2018626596Oclk48&returnType=2&count=1'
    r = requests.get(url,headers=headers,cookies=cookies)
    r.encoding = 'utf-8'
    time.sleep(1)
    result= r.json()
    proxies = result['RESULT']
    for proxie in proxies:
        ip = proxie['ip']
        port = proxie['port']
        proxies = {
            'http': "http://" +ip + ':' +port
        }
        #proxies = 'http://'+ ip + ':' +port
    print(proxies)
    url1 = 'http://icanhazip.com/'
    response = requests.get(url1, headers=headers, proxies=proxies)
    ip = response.text.replace('\n', '')
    print(ip)



    #print(proxies)
# def get_page(url):
#     r = requests.get(url)
#     r.encoding = 'utf-8'
#     return r

    #url = 'http://www.glidedsky.com/level/web/crawler-ip-block-1'
if __name__ == '__main__':
    crawl_xdaili()
    #get_page(url)

# import requests
#
# # 代理服务器
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
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
# }
# url = 'http://icanhazip.com/'
# response = requests.get(url, headers=headers, proxies=proxies)
# ip = response.text.replace('\n', '')
# print(ip)
