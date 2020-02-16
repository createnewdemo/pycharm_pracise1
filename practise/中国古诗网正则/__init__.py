import requests
import re


def parse_url(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    r = r.text
    names = re.findall(r'<a\sstyle="font-size:18px; line-height:22px; height:22px;".*?<b>(.*?)<\/b>', r, re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source".*?<a.*?target="_blank">(.*?)</a>', r, re.DOTALL)
    authors = re.findall(r'<p\sclass="source".*?<a.*?</a>.*?target="_blank">(.*?)</a>', r, re.DOTALL)
    content_tags = re.findall(r'<div\sclass="contson" id=".*?">(.*?)</div>', r, re.DOTALL)
    # print(content_tags)
    poems = []
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>', "", content, re.DOTALL)
        # print(x.strip())
        contents.append(x.strip())  # strip 去掉空白与换行
    # print(contents)
    for value in zip(names, dynasties, authors, contents):
        name, dynasity, author, content = value
        poem = {
            '诗名': name,
            '朝代': dynasity,
            '作者': author,
            '内容': content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print('=' * 40)


def main():
    urls = 'https://www.gushiwen.org/default_{}.aspx'
    for i in range(1, 11):
        url = urls.format(i)
        parse_url(url)


main()
