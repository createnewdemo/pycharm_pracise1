from lxml import etree


def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse("拉钩网py.html", parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


def main():
    parse_lagou_file()


main()
