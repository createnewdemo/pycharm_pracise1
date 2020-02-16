import requests
import json

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://www.hnuahe.edu.cn/',
    'Connection': 'keep-alive',
}
cookies = {
    'JSESSIONID': 'ED054EB7D633F5E2239D61F196854714',
}
start_url = "http://www.hnuahe.edu.cn/"


def get_url(url):
    r = requests.get(url, headers=headers, cookies=cookies)
    r.encoding = 'utf-8'
    r = r.text
    return r


def parse_url(r):
    pass


def main():
    url = "http://www.hnuahe.edu.cn/"
    get_url(url)


main()
