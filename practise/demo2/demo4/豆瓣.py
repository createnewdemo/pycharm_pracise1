# encoding:utf-8
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Referer': 'https://movie.douban.com/',

}
url = 'https://movie.douban.com/cinema/nowplaying/xinyang/'
r = requests.get(url, headers=headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
r = r.text
html = etree.HTML(r)  # 解码  然后可使用xpath
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))
lis = ul.xpath("./li")
# title = lis.xpath("@data-title")
movies = []
# print(etree.tostring(lis,encoding='utf-8').decode("utf-8"))
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode("utf-8"))
    title = li.xpath("@data-title")
    wish = li.xpath("@data-wish")
    region = li.xpath("@data-region")
    actors = li.xpath("@data-actors")
    movie = {
        '名字': title,
        '想看人数': wish,
        '国家': region,
        '演员': actors
    }
    movies.append(movie)
print(movies)
