import re

import requests


def verify():
    cookies = {
        'UM_distinctid': '170a9417a21b97-06c091463e1b94-3a614f0b-1fa400-170a9417a2266',
        'PHPSESSID': '0',
        'healAjax': '0',
        'name': '0',
        'utid': '0',
        'uuid': '0',
        'uin': '0',
        'sid': 'fHp3NT84',
        'schoolExt': '53',
        'schoolType': '1',
        'schoolName': '%E6%B2%B3%E5%8D%97%E7%89%A7%E4%B8%9A%E7%BB%8F%E6%B5%8E%E5%AD%A6%E9%99%A2',
        'CNZZDATA1264334274': '0%7C1583387663',
        'type': '1',
        'uniName': '%E5%8C%85%E8%A3%85%E4%B8%8E%E5%8D%B0%E5%88%B7%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2',
        'uerrExpire': '1583388969',
        'uerrNum': '0',
        'ulauth': '631c0ca9288731359da294f88b53c147',
        'uvauth': '4f47d866ba02ceb1a3c7ef3f480d9733',
    }

    headers = {
        'Origin': 'http://jktb.haedu.gov.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'timestamp': '1583388696002',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'http://jktb.haedu.gov.cn/?act=verify',
    }

    params = (
        ('act', 'verify'),
    )

    data = {
      'do': 'check',
      'str': '4f47d866ba02ceb1a3c7ef3f480d9733',
      'mobile': '17190199811',
      'idCard': '2710',
      'rn': '0.012986855361587502'
    }
    s = requests.Session()
    r = s.post('http://jktb.haedu.gov.cn/?act=verify', headers=headers, params=params, cookies=cookies, data=data)

    r = r.text

    con = re.findall(r'"msg":"(.+)",', r)[0]

    print(con.encode('utf-8').decode('unicode_escape'))
    return s
def sub():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'timestamp': '1583389172414',
        'Origin': 'http://jktb.haedu.gov.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://jktb.haedu.gov.cn/?act=health',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    params = (
        ('act', 'health'),
    )

    data = {
      'regYmd': '2020-04-09',
      'regProvince': '490000',
      'regCity': '491500',
      'regArea': '491524',
      'isCunDiag': '0',
      'isToge': '0',
      'cunAddr': '',
      'togeAddr': '',
      'isGoHb': '0',
      'goCity': '0',
      'goYmd': '',
      'isTouch': '0',
      'touchProvince': '0',
      'touchCity': '0',
      'touchArea': '0',
      'touchAddr': '',
      'touchYmd': '',
      'isObs': '0',
      'isDiag': '0',
      'diagYmd': '1970-01-01',
      'diagHospital': '',
      'CureYmd': '',
      'isGood': '1',
      'whatSitua': '',
      'cunWhere': '1',
      'touchWhere': '0',
      'do': 'ajax'
    }
    s = verify()
    r = s.post('http://jktb.haedu.gov.cn/?act=healok', headers=headers, params=params, data=data)

    r = r.text

    con = re.findall(r'"msg":"(.+)",', r)[0]

    print(con.encode('utf-8').decode('unicode_escape'))



sub()