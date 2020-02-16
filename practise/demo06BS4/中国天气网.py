import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar

ALL_DATA = []


def parse_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    r = r.text
    soup = BeautifulSoup(r, 'html5lib')  # html5lib 这个解析器比较稳
    infos = soup.find("div", "conMidtab")
    table = infos.find_all("table")
    # print(table)
    for trs in table:
        trs = trs.find_all("tr")[2:]
        for index, tds in enumerate(trs):
            tds = tds.find_all("td")
            citys_td = tds[0]
            if index == 0:
                citys_td = tds[1]
            city = list(citys_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})  # 转为整型  好排序
            # print({'city':city,'min_temp':int(min_temp))


def main():
    urls = 'http://www.weather.com.cn/textFC/{}.shtml'
    ads = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']

    # print(ad[0])

    for ad in ads:
        url = urls.format(ad)
        # print(url)
        parse_url(url)
        ALL_DATA.sort(key=lambda data: data['min_temp'], reverse=True)  # 匿名函数
        data = ALL_DATA[0:10]
        cities = list(map(lambda x: x['city'], data))
        temps = list(map(lambda x: x['min_temp'], data))
        # print(cities)
        # print(temps)
        chart = Bar()
        chart.add_xaxis(cities)
        chart.add_yaxis("温度", temps)  # 前面的参数是注释 圆柱表示啥
        chart.render('temperature.html')


main()
