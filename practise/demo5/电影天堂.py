from lxml import etree
import requests

# url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Host': 'www.dytt8.net'
}
BASE_DOMAIN = 'https://www.dytt8.net/'


def get_detail_urls(url):
    r = requests.get(url, headers=HEADERS)
    # r.raise_for_status()
    # print(r.text)
    # print(r.status_code)
    r = r.text
    html = etree.HTML(r)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    return detail_urls


def parse_detail_page(url):  # 解析详情页面
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    r = r.text
    html = etree.HTML(r)
    title = html.xpath("div[@class='title_all']//font[@color='#07519a']/text()")[0]
    print(title)


def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1, 8):  # 产生1-7的列表
        url = base_url.format(x)  # 构建完整url  返回url作为参数给get_detail_urls(url)函数调用
        detail_urls = get_detail_urls(url)  # 解析详情页面  返回详情页面列表类型
        for detail_url in detail_urls:  # 产生电影详情页
            movie = parse_detail_page(detail_url)
            break
        break


if __name__ == '__main__':
    spider()
