import requests
import re


def getHTMLText(url):  # 获取页面信息
    try:
        header = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cache-control': 'max-age=0',
            'authority': 's.taobao.com',
            'cookie': 'thw=cn; cna=IYLVFcBiOWcCAXM5jN3K0OHq; miid=449994171888546622; t=549bbd46758cd61cf0c1518fea6eac39; cookie2=1c0844be0d590d93ddabf4ab9eae9a7a; v=0; _tb_token_=5e757553b576b; _samesite_flag_=true; unb=2215169717; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=o%2FMhwdoo%2BXM%3D&id2=UUpgQyjvsYcKlQ%3D%3D&vt3=F8dBxdsSGWiLoDeKVQU%3D; csg=da4d06f7; lgc=%5Cu674E%5Cu4E16%5Cu6797%5Cu4EBA; cookie17=UUpgQyjvsYcKlQ%3D%3D; dnk=%5Cu674E%5Cu4E16%5Cu6797%5Cu4EBA; skt=0b92c0639e68e0d1; existShop=MTU4MDQ0NzAwOQ%3D%3D; uc4=nk4=0%40oaXqHgV1Zl6qjpZkLaTj2SqlRg%3D%3D&id4=0%40U2gqzJ64xKcxdqIQYf5yrSJPaqef; tracknick=%5Cu674E%5Cu4E16%5Cu6797%5Cu4EBA; _cc_=W5iHLLyFfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E4%BA%BA79; _nk_=%5Cu674E%5Cu4E16%5Cu6797%5Cu4EBA; cookie1=VWfDgahuW0CCm3fPL2auNzf6gv2GdGpTNK5vdi5huwc%3D; enc=l4h7ak0nFcXzCujWFBsWnCNyvHwnhKlT9IarjHMysjknDattS67emREQ1exuN%2Fmt0dcqg7vfpabrtodia0Escw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=87_1; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=W5iHLLyFe3xm&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTUOqS5outd6Q%3D%3D&cart_m=0&tag=8&lng=zh_CN; l=cBgGh7nuqX7prKTtBOCZ5uI8Lu7TRIRfguPRwCYMi_5Qu6Y1ozbOoqYn4Fv6cjWFGF8B4IQ3FveTVeEg-yWjJ0YEae1VivC..; isg=BNHRDhpSa9OTyYRzDP85hXaG4N1rPkWwUs2rP7Nm4Bi1WvCs-47PgXF4_C680t3o; JSESSIONID=7F1224E2E5F2B11025060A26149012E3',
        }

        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        # print(r.status_code)
        return r.text
    except:
        print("爬取失败")
        return ""


def parsePage(ilt, html):  # 获取商品价格信息"view_price":"59.00"\ "raw_title":""
    try:  # 用try except 使程序稳定 不会因为程序出错而退出程序
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # 返回的是列表类型
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # [0,1]
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("解析出错")


def printGoodsList(ilt):  # 输出信息到屏幕上
    tplt = "{:4}\t{:8}\t{:16}"  # \t代表4个空字符相当于tab
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = input('请输入要获取价格的商品：')
    depth = 2  # 爬取的深度 （页数）
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
            # print(url)
        except:
            continue
    printGoodsList(infoList)


main()
