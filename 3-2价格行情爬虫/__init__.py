# -*- coding: gbk -*-
import pymysql
import requests
from lxml import etree

start_url = ['http://www.xinfadi.com.cn/marketanalysis/0/list/{}.shtml'.format(str(i)) for i in range(0, 9217)]


def parseOnePage(url):
    # url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
    r = requests.get(url)
    html = etree.HTML(r.content)
    # print(html)
    list = []
    infos = html.xpath("//table[@class='hq_table']/tr")
    i = 1
    for info in infos[1:]:
        title = info.xpath("./td/text()")
        name = title[0]
        min = title[1]
        average = title[2]
        max = title[3]
        specification = title[4]
        unit = title[5]
        time = title[6]
        source = {
            'name': name,
            'min': min,
            'average': average,
            'max': max,
            'specification': specification,
            'unit': unit,
            'time': time,
        }
        list.append(title)
        print(name)

        conn = pymysql.connect(host='localhost', user='root', password='admin', database='py_mysql_demo', port=3306)
        cursor = conn.cursor()
        sql = """
        insert into price(id,name,min,average,max,specification,unit,time) values(NULL,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (
            source['name'], source['min'], source['max'], source['average'], source['specification'], source['unit'],
            source['time']))
        conn.commit()
        print('=' * 5 + '存入数据库成功,本次为第%d数据' % i)
        i += 1
    conn.close()


def main():
    i = 1
    for url in start_url:
        parseOnePage(url)
        print("第%d页获取完成" % i)
        i += 1


if __name__ == '__main__':
    main()
