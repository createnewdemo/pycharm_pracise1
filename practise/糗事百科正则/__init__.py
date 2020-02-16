import requests
import re
import csv


def parse_url(url):
    r = requests.get(url)
    r.encoding = 'zh-CN'
    r = r.text
    Content = []
    content_list = []
    authors = re.findall(r'<h2>\s(.*?)\s</h2>', r)
    contents = re.findall(r'<div class="content">(.*?)</a>', r, re.S)
    # print(authors)
    for content in contents:
        x = re.sub(r'<.*?>', "", content, re.S)
        content_list.append(x.strip())

    for value in zip(authors, content_list):
        author, content = value
        content = {
            'author': author,
            'content': content
        }
        Content.append(content)
        # print(Content)
    for s in Content:
        print(s)
        print('=' * 40)
    headers = ['author', 'content']

    # with open('qs.csv','w',encoding='utf-8',newline='') as fp:
    #     writer = csv.DictWriter(fp,headers)
    #     #手动写入表头
    #     writer.writeheader()
    #     writer.writerows(s)


def main():
    urls = 'https://www.qiushibaike.com/text/page/{}/'
    for i in range(1, 11):
        url = urls.format(i)
        parse_url(url)


main()
