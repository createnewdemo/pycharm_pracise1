import requests

url = "https://www.amazon.cn/dp/B01N4P9MT5/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E9%9D%9E%E6%9A%B4%E5%8A%9B%E6%B2%9F%E9%80%9A&qid=1580181744&sr=8-1"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
