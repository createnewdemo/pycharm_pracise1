import requests
# import pymysql
import time
import csv
import json

xx = []
start_url = [
    'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(
        str(i)) for i in range(0, 320, 20)]
class douban(object):
    def __init__(self):
        self.cookies = {
            'bid': 'MMY0DyntCxs',
            'douban-fav-remind': '1',
            '__yadk_uid': 'mfd3BzX4pPhYKlU4u7QN5UHihiIaGlFQ',
            'll': '118251',
            '__gads': 'ID=e90a02f8030b8f3c:T=1580805941:S=ALNI_MYBRD6yXLD8dRSow16DVtCY8bR15w',
            'push_noty_num': '0',
            'push_doumail_num': '0',
            'douban-profile-remind': '1',
            '_vwo_uuid_v2': 'DD24C23AE44130D99CDC9F04E361A80B1|7f3d3ce76278ddfe3227703d0b960424',
            '__utmc': '30149280',
            'ap_v': '0,6.0',
            'dbcl2': '211373509:5gtrDYpsPPM',
            'ck': 'tlMg',
            '__utmv': '30149280.21137',
            '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1581914826%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Fregister%22%5D',
            '_pk_ses.100001.8cb4': '*',
            '__utma': '30149280.372476684.1565432915.1581908548.1581914826.14',
            '__utmz': '30149280.1581914826.14.10.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/register',
            '__utmt': '1',
            '_pk_id.100001.8cb4': 'b6e674f0b03477b1.1573117061.14.1581914829.1581908829.',
            '__utmb': '30149280.4.10.1581914826',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }

        self.data = {
            'type': 'movie',
            'tag': '热门',
            'sort': 'recommend',
            'page_limit': '20',
            'page_start': '0',
        }

    """
    获取url
    """

    def crawl_xdaili(self):
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
        r = requests.get(url, headers=headers, cookies=cookies)
        r.encoding = 'utf-8'
        #time.sleep(1)
        result = json.loads(r.text)
        proxies = result['RESULT']
        print("这里出错没有")
        for proxie in proxies:
            ip = proxie['ip']
            port = proxie['port']
            proxies = {
                'http': "http://" + ip + ':' + port
            }

            # proxies = 'http://'+ ip + ':' +port
        print(proxies)
        url1 = 'http://icanhazip.com/'
        response = requests.get(url1, headers=headers, proxies=proxies,timeout = 5)
        ip = response.text.replace('\n', '')
        print(ip)

        return result

    def get_url(self, url):
        # self.daili(proxies)
        #time.sleep(1)
        r = requests.get(url, headers=self.headers, cookies=self.cookies, data=self.data)
        r.encoding = 'utf-8'

        #result = r.json()
        result = json.loads(r.text)
        return result

    """
    解析页面ajsx的页面
    """

    def parse_page(self, result, m):
        # print(result)
        infos = result['subjects']
        #time.sleep(1)
        for i in range(0, 20):
            info = infos[i]
            name = info['title']
            score = info['rate']
            detail_url = info['url']
            # print(detail_url)
            x = {
                'name': name,
                'score': score,
                'detail_url': detail_url
            }
            print(x)
            xx.append(x)
            headers = ['name', 'score', 'detail_url']
            with open('douban.csv', 'w') as fp:
                f_csv = csv.DictWriter(fp, headers)
                f_csv.writeheader()
                f_csv.writerows(xx)

            # break
            # self.save_info(x,)

    def save_info(self, x):
        xx = []
        xx.append(x)
        headers = ['name', 'score', 'detail_url']
        with open('douban.csv', 'w') as fp:
            f_csv = csv.DictWriter(fp, headers)
            f_csv.writeheader()
            f_csv.writerows(xx)


#         conn = pymysql.connect(host='localhost', user='root', password='root', database='py_mysql_demo', port=3306)
#         cursor = conn.cursor()
#         try:
#             sql = """
#             insert into douban(id,name,score,url) values(NULL,%s,%s,%s)
#             """
#             cursor.execute(sql,(x['name'],x['score'],x['detail_url']))  # 执行   第二个参数以元组的方式传入
#             conn.commit()
#             print('='*5+x['name']+'='*5+'存入数据库成功,本次为第%d数据'%i)
#             conn.close()
#         except Exception as e:
#             print(e)
#             print('插入数据库失败')
def main():

    try:

        i = 0
        for url in start_url:

            i += 1
            spider = douban()
            result_ip=spider.crawl_xdaili()
            if result_ip:
                result = spider.get_url(url)
                spider.parse_page(result, i)
            else:
                exit()
            # spider.save_info(x,i)
            # break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
