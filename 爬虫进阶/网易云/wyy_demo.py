# from DecryptLogin import login
# l = login.Login()
# session = l.douban('17190199811', 'lsl723723', 'pc')
import requests
from lxml import etree

cookies = {
    'bid': 'MMY0DyntCxs',
    '__yadk_uid': 'AnRqFcOedSAeTWY1JM93xQD1Yq8jrjol',
    'trc_cookie_storage': 'taboola%2520global%253Auser-id%3Dbb7f7e92-894a-4b67-8de3-9a3c8d7d9618-tuct44821d1',
    'douban-fav-remind': '1',
    'll': '118251',
    '__gads': 'ID=e90a02f8030b8f3c:T=1580805941:S=ALNI_MYBRD6yXLD8dRSow16DVtCY8bR15w',
    'push_noty_num': '0',
    'push_doumail_num': '0',
    '__utmv': '30149280.16028',
    'douban-profile-remind': '1',
    '_vwo_uuid_v2': 'DD24C23AE44130D99CDC9F04E361A80B1|7f3d3ce76278ddfe3227703d0b960424',
    '__utma': '30149280.372476684.1565432915.1581755861.1581774679.10',
    '__utmc': '30149280',
    '__utmz': '30149280.1581774679.10.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'dbcl2': '160285873:12Za5hhsr6U',
    'ck': 'Qe-C',
    '__utmb': '30149280.3.10.1581774679',
    'ap_v': '0,6.0',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1581774692%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.4cf6': '*',
    '_pk_id.100001.4cf6': '7a1ba3fef3a68ae6.1565432919.4.1581775041.1581641644.',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
r = requests.get("https://www.douban.com/", headers=headers, cookies=cookies)
r.encoding = 'utf-8'
print(r.text)
html = etree.HTML(r.text)
wd = html.xpath("//*[@id='db-nav-sns']/div/div/div[3]/ul/li[1]/a/text()")
print(wd)
