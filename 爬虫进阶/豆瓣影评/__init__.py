import requests
import pymysql
import time

start_url = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(str(i))for i in range(0,6001,20)]
class douban(object):
    def __init__(self):
        self.cookies = {
    'bid': 'MMY0DyntCxs',
    '__yadk_uid': 'AnRqFcOedSAeTWY1JM93xQD1Yq8jrjol',
    'trc_cookie_storage': 'taboola%2520global%253Auser-id%3Dbb7f7e92-894a-4b67-8de3-9a3c8d7d9618-tuct44821d1',
    'douban-fav-remind': '1',
    'll': '118251',
    '__gads': 'ID=e90a02f8030b8f3c:T=1580805941:S=ALNI_MYBRD6yXLD8dRSow16DVtCY8bR15w',
    'push_noty_num': '0',
    'push_doumail_num': '0',
    '__utmv': '30149280.16028',
    'douban-profile-remind': '1',
    '_vwo_uuid_v2': 'DD24C23AE44130D99CDC9F04E361A80B1|7f3d3ce76278ddfe3227703d0b960424',
    '__utma': '223695111.910971417.1565432915.1581641644.1581774692.4',
    '__utmz': '223695111.1581774692.4.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1581774692%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_id.100001.4cf6': '7a1ba3fef3a68ae6.1565432919.4.1581775419.1581641644.',
    'ap_v': '0,6.0',
    '__utmc': '30149280',
    'dbcl2': '160285873:12Za5hhsr6U',
    'ck': 'Qe-C',
    '__utmt': '1',
    '__utmb': '30149280.2.10.1581819469',
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
    def get_url(self,url):
        time.sleep(1)
        r = requests.get(url,headers=self.headers,cookies=self.cookies,data=self.data)
        r.encoding = 'utf-8'
        result= r.json()
        return result
    """
    解析页面ajsx的页面
    """
    def parse_page(self,result,m):
        xx = []
        #print(result)
        infos = result['subjects']
        #time.sleep(1)
        for i in range(0,20):
            info = infos[i]
            name = info['title']
            score = info['rate']
            detail_url = info['url']
            #print(detail_url)
            x = {
                'name':name,
                'score':score,
                'detail_url':detail_url
            }
            self.save_info(x,m)
    def save_info(self,x,i):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='py_mysql_demo', port=3306)
        cursor = conn.cursor()
        try:
            sql = """
            insert into douban(id,name,score,url) values(NULL,%s,%s,%s)
            """
            cursor.execute(sql,(x['name'],x['score'],x['detail_url']))  # 执行   第二个参数以元组的方式传入
            conn.commit()
            print('='*5+x['name']+'='*5+'存入数据库成功,本次为第%d数据'%i)
            conn.close()
        except Exception as e:
            print(e)
            print('插入数据库失败')
def main():
    try:
        i=0
        for url in start_url:
            i += 1
            spider = douban()
            result = spider.get_url(url)
            spider.parse_page(result,i)
            #spider.save_info(x,i)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()


