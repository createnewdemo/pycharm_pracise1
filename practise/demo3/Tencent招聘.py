from lxml import etree

# 获取所有a标签
# 获取第2个tr标签
# 获取所有class等于even的标签
# 获取所有的职位信息（纯文本）
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("Tencent招聘.html", parser=parser)
# 获取所有a标签  //a.
# xpath返回的是一个列表
'''As = html.xpath("//a")
for a in As:
    print(etree.tostring(a,encoding='utf-8').decode("utf-8"))#tostring 转化为字符串'''
positions = []
tits = html.xpath("//h4")
for tit in tits:
    title = tit.xpath(".//a/text()")

infos = html.xpath("//p[1]")
# print(infos)
for info in infos:
    info = info.xpath(".//text()")  # p标签下的所有文本用//
    print(info)

    # info1 = info.xpath(./)'''
