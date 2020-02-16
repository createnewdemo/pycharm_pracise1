from lxml import etree
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
url = 'https://www.icourse163.org/learn/BIT-1001870001?tid=1206951268#/learn/content?type=detail&id=1211970247&cid=1215042945'
r = requests.get(url, headers=HEADERS)
r.encoding = 'utf-8'
r = r.text
soup = BeautifulSoup(r, "lxml")
links = soup.find_all('link', rel='dns-prefetch')
for link in links:
    print(link)
    print('=' * 30)

# def get_urls(url):
#     try:
#         r = requests.get(url,timeout=30,headers=HEADERS)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         html = etree.HTML(r.text)
#         #print(type(r.text))
#         return html
#     except:
#         print("error")
#
# def parse_Page_get_info(rText):
#     print(rText)
#     #html = etree.HTML(rText)
#     #print(html.tag)
#     infos = rText.xpath("//div[@class='recruit-list']")
#     print(infos)
#     for info in infos:
#         href = info.xpath(".//a")
#         print(href)
#
#


# def print_infos():
#     pass
# def main(page):#page  可选择爬取多少页面
#     if page == 1:
#         BASE_URLS = 'https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006'
#         BASE_URL  = BASE_URLS
#         rText = get_urls(BASE_URL)
#         #print(type(rText))
#         #print(rText)
#         parse_Page_get_info(rText)#解析页面
#
#     else:
#         for i in range(1, page+1):
#             BASE_URLS = 'https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006&index={}'
#             BASE_URL = BASE_URLS.format(i)
#             html = get_urls(BASE_URL)
#             #print(type(html))
#             parse_Page_get_info(html)
# main(page=1)
#
