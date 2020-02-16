# http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html
# 爬取中国大学2019的排名信息，爬取‘排名’，‘学校名’，‘省份’，‘总分’，这四个字段信息
# 我们代码与 ‘bs4 提取’ 章节，类似，只有部分需要修改
import requests
import time
from lxml import etree


def get_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('error')


def get_infos(html):
    html = etree.HTML(html)
    ls = html.xpath('//tr[@class="alt"]')
    # 使用 xpath 方法选择标签在 html 源码里的路径，\
    # // 是选择此 html 源码里所有 tr 标签并且 class 属性为 alt 的标签
    for info in ls:
        # ‘.’ 代表当前节点，就是对应的每次循环的这个标签的节点

        #   ‘/’ 依次选择路径
        # 排名
        rank = info.xpath('./td[1]/text()')[0]
        # 学校名
        name = info.xpath('./td[2]/div/text()')[0]
        # 省份
        province = info.xpath('./td[3]/text()')[0]
        # 总分
        score = info.xpath('./td[4]/text()')[0]
        data = {
            '排名': rank,
            '校名': name,
            '省份': province,
            '总分': score,
        }
        print(data)


def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = get_html(url)
    get_infos(html)

    time.sleep(1)


if __name__ == '__main__':
    main()
