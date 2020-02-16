import json
import time
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
}


class lagou:
    def __init__(self):
        self.ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        self.params = {
            "first": "true",
            "pn": 1,
            "kd": "python",
        }

    def get_cookies(self):
        cookie_url = "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="  # 请求的地址就是reference
        session = requests.Session()
        time.sleep(2)
        session.get(url=cookie_url)
        print(session.cookies)
        return session.cookies

    def parse_url(self):
        response = requests.post(url=self.ajax_url, headers=headers, data=self.params, cookies=self.get_cookies())
        time.sleep(2)
        json_str = json.loads(response.text)
        print(self.get_cookies())
        print(self.params)
        print(json_str)

    def run(self):
        time.sleep(2)
        self.parse_url()

        # pass


if __name__ == '__main__':
    la = lagou()
    la.run()
