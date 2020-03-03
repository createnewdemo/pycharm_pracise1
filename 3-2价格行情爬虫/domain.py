import requests
from lxml import etree


# url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
#
# r = requests.get(url)
#
# #print(r.text)
# html = etree.HTML(r.content)
# print(html)
#
# info = html.xpath("//table[@class='hq_table']//tr[1]").text()
# #name = info.xpath()
# print(info)

class price(object):

    def __init__(self):
        self.url = ["http://www.xinfadi.com.cn/marketanalysis/0/list/{}.shtml"].format()

    def parseOnePage(self):
        pass

    def parseOneInfo(self):
        pass

    def SaveInfo(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    spider = price()
    spider.run()
