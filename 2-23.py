import requests
from bs4 import BeautifulSoup

cookies = {
    'ASP.NET_SessionId': 'oifd5gzvdhjhhob3mh5v5yc0',
    'Hm_lvt_83853859c7247c5b03b527894622d3fa': '1582460741',
    'security_session_verify': '7241daf3b318ddf9545cd7181f91cba4',
    'srcurl': '68747470733a2f2f7777772e6c616e646368696e612e636f6d2f4465736b746f704d6f64756c652f42697a6672616d65457874656e644d646c2f776f726b4c6973742f62756c576f726b566965772e617370783f776d677569643d32306161653864632d346130632d346166352d616564662d636331353365623665666466267265636f72646572677569643d32616566663633392d663737662d346632322d396234372d3437356164643463646136312673697465506174683d',
    'security_session_mid_verify': 'f359f7d90735402892fb65f08053bd44',
    'Hm_lpvt_83853859c7247c5b03b527894622d3fa': '1582465098',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&recorderguid=2aeff639-f77f-4f22-9b47-475add4cda61&sitePath=&security_verify_data=313932302c31303830',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

params = (
    ('wmguid', '20aae8dc-4a0c-4af5-aedf-cc153eb6efdf'),
    ('recorderguid', '2aeff639-f77f-4f22-9b47-475add4cda61'),
    ('sitePath', ''),
)

r = requests.get('https://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx', headers=headers,
                 params=params, cookies=cookies)
r.encoding = 'gbk'
print(r.text)
soup = BeautifulSoup(r.text.replace('&nbsp;', ' '), "lxml")
