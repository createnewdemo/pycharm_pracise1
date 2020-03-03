import requests
import json
import jsonpath
from lxml import etree
import csv
import time
import itertools
from fake_useragent import UserAgent
import random
import pandas as pd

requests.packages.urllib3.disable_warnings()


class Spider(object):
    def crawl_xdaili(self):
        url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=62258522ca084c20abccfb1028f6ad7e&orderno=YZ2018626596Oclk48&returnType=2&count=1'
        r = requests.get(url)
        if r:
            result = json.loads(r.text)
            proxies = result.get('RESULT')
            for proxy in proxies:
                # print(proxy.get('ip'))
                # print(proxy.get('port'))
                proxies = {
                    'http': 'http://' + proxy.get('ip') + ":" + proxy.get('port')
                }
                # print(proxies)
                return proxies

    def get_html(self):
        try:
            cookies = {
                'security_session_verify': 'f096ca7a556e56a181dd59ea4ca10c4d',
                'security_session_mid_verify': '58c6c64dbdb14500e2e92042d057e0a5',
                'Hm_lvt_83853859c7247c5b03b527894622d3fa': '1582631582,1582634737',
                'ASP.NET_SessionId': 'nck0jxv0xntm2r1qyquv5cq3',
                'Hm_lpvt_83853859c7247c5b03b527894622d3fa': '1582634737',
            }

            headers = {
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                'Sec-Fetch-User': '?1',
                'Origin': 'https://www.landchina.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Referer': 'https://www.landchina.com/default.aspx?tabid=261&ComName=default',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
            }

            params = (
                ('tabid', '261'),
                ('ComName', 'default'),
            )
            proxies = self.crawl_xdaili()
            print(proxies)
            # session = requests.session()
            # session.get('https://www.landchina.com/default.aspx', headers=headers)
            response = requests.get('https://www.landchina.com/default.aspx?tabid=261&ComName=default', headers=headers,
                                    params=params,
                                    cookies=cookies, proxies=proxies)
            r = response.text
            html = etree.HTML(r)
            xinxis = html.xpath('//div[@id="clock"]')
            print(xinxis)
        except Exception as e:
            print(e)

    def get_surls(self, html):
        try:
            infos = []
            html = etree.HTML(html)
            xinxis = html.xpath('//tr[@onmouseout="this.className=rowClass"]')
            print(len(xinxis))
            for xinxi in xinxis:
                title = xinxi.xpath('./td[3]/a/span/@title')[0]
                lianjie = 'https://www.landchina.com/' + xinxi.xpath('./td[3]/a/@href')[0]
                fangshi = xinxi.xpath('string(./td[4])')
                riqi1 = xinxi.xpath('string(./td[5])')
                riqi2 = xinxi.xpath('string(./td[6])')
                data = {
                    '0': lianjie,
                    '1': title,
                    '2': fangshi,
                    '3': riqi1,
                    '4': riqi2
                }
                print(data)
                infos.append(data)
            ccc = pd.DataFrame.from_dict(infos)
            ccc.to_csv('muluye.csv', mode='a', encoding='utf-8-sig', header=False, index=False)
            '''
            ccc = pd.DataFrame.from_dict(infos)
            ccc.to_csv('urls2.csv', mode='a', encoding='utf-8-sig', header=False, index=False)'''
            time.sleep(random.uniform(3, 5))
        except Exception as e:
            print(e)
            time.sleep(random.uniform(3, 5))

    # 41,91
    def main_run(self):
        count = 0
        lis = [i for i in range(6, 7)]
        for li in lis:
            data = [
                ('__VIEWSTATE',
                 '/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhwFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBYwBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2NyZ2cyMDExTkhfMDEuZ2lmKTsfAwUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwF/AY8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHBzOi8vd3d3LmxhbmRjaGluYS5jb20vIj48aW1nIGJvcmRlcj0iMCIgYWx0PSIiIHdpZHRoPSIyNjAiIGhlaWdodD0iNjEiIHNyYz0iL1VzZXIvZGVmYXVsdC9VcGxvYWQvZmNrL2ltYWdlL3Rkc2N3X2xvZ2UucG5nIiAvPjwvYT4mbmJzcDs8YnIgLz4NCiZuYnNwOzxzcGFuIHN0eWxlPSJjb2xvcjogI2ZmZmZmZiI+Q29weXJpZ2h0IDIwMDgtMjAxOSBEUkNuZXQuIEFsbCBSaWdodHMgUmVzZXJ2ZWQmbmJzcDsmbmJzcDsmbmJzcDsgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KdmFyIF9iZGhtUHJvdG9jb2wgPSAoKCJodHRwczoiID09IGRvY3VtZW50LmxvY2F0aW9uLnByb3RvY29sKSA/ICIgaHR0cHM6Ly8iIDogIiBodHRwczovLyIpOw0KZG9jdW1lbnQud3JpdGUodW5lc2NhcGUoIiUzQ3NjcmlwdCBzcmM9JyIgKyBfYmRobVByb3RvY29sICsgImhtLmJhaWR1LmNvbS9oLmpzJTNGODM4NTM4NTljNzI0N2M1YjAzYjUyNzg5NDYyMmQzZmEnIHR5cGU9J3RleHQvamF2YXNjcmlwdCclM0UlM0Mvc2NyaXB0JTNFIikpOw0KPC9zY3JpcHQ+Jm5ic3A7PGJyIC8+DQrniYjmnYPmiYDmnIkmbmJzcDsg5Lit5Zu95Zyf5Zyw5biC5Zy6572RJm5ic3A7Jm5ic3A75oqA5pyv5pSv5oyBOua1meaxn+iHu+WWhOenkeaKgOiCoeS7veaciemZkOWFrOWPuCZuYnNwOzxiciAvPg0K5aSH5qGI5Y+3OiDkuqxJQ1DlpIcwOTA3NDk5MuWPtyDkuqzlhaznvZHlronlpIcxMTAxMDIwMDA2NjYoMikmbmJzcDs8YnIgLz4NCjwvc3Bhbj4mbmJzcDsmbmJzcDsmbmJzcDs8YnIgLz4NCiZuYnNwOzwvc3Bhbj48L3A+HwEFZEJBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3cyMDEzX3l3XzEuanBnKTtkZFYJyUlUNviC7mK/FHZHuG03g0vGc2fj0FUhWrBJcFyP'),
                ('__EVENTVALIDATION',
                 '/wEdAAJDgrlTIbHDRNvE11Y4EqVOCeA4P5qp+tM6YGffBqgTjVgiaCy62ZlA3B3rxyfk9BO43Gv4h9zvbmM7KDnnEuKc'),
                ('hidComName', 'default'),
                ('TAB_QueryConditionItem', '598bdde3-078b-4c9b-b460-2e0b2d944e86'),
                ('TAB_QueryConditionItem', '87f11024-55ab-4faf-a0af-46371e33ae66'),
                ('TAB_QuerySubmitConditionData', '598bdde3-078b-4c9b-b460-2e0b2d944e86:2020-1-1~2020-1-31'),
                ('TAB_QuerySubmitOrderData', ''),
                ('TAB_RowButtonActionControl', ''),
                ('TAB_QuerySubmitPagerData', str(li)),
                ('TAB_QuerySubmitSortData', ''),
            ]
            count += 1
            print(count)
            html = self.get_html(data)
            self.get_surls(html)
            time.sleep(5)


if __name__ == '__main__':
    spider = Spider()
    # spider.main_run()
    # spider.crawl_xdaili()
    spider.get_html()
