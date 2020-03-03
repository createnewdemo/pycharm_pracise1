# -*- coding: gbk -*-
import requests
import random
import os
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm

from openpyxl import Workbook

i = 0


class weater_demo(object):
    def __init__(self):
        self.infos = [{
            'qq邮箱': '2530112392@qq.com',
            '地区': '信阳',
        }, {
            'qq邮箱': '1070647680@qq.com',
            '地区': '洛阳',
        },
            {
                'qq邮箱': '584366615@qq.com',
                '地区': '郑州',
            },
            {
                'qq邮箱': '1429483153@qq.com',
                '地区': '信阳',
            },
            {
                'qq邮箱': '519252626@qq.com',
                '地区': '安阳',
            },

        ]
        # 获取当日时间	2020-2-17
        self.today_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.text = ""
        self.user_agent = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
            "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
            "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
            "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
            "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
            "UCWEB7.0.2.37/28/999",
            "NOKIA5700/ UCWEB7.0.2.37/28/999",
            "Openwave/ UCWEB7.0.2.37/28/999",
            "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
            # iPhone 6：
            "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
        ]

    def get_url(self):  # 获取地区接口
        urls = []
        for self.inx, val in enumerate(self.infos):
            # print(inx)
            self.url = 'https://free-api.heweather.net/s6/weather/forecast?location={}&key=3f8659a2ab674ca6bdc3e740462a6ae1'.format(
                self.infos[self.inx]['地区'])
            urls.append(self.url)
        print(urls[i])
        return urls[i]

    def get_weather_data(self):
        url = self.get_url()
        res = requests.get(url).json()
        result = res['HeWeather6'][0]['daily_forecast']
        city = res['HeWeather6'][0]['basic']['parent_city']  # +res['HeWeather6'][0]['location']
        province = res['HeWeather6'][0]['basic']['admin_area']
        datas = []
        for data in result:  # 三天的
            date = data['date']  # 获取日期
            cond = data['cond_txt_d']  # 天气情况
            max = data['tmp_max']  # 最高温度
            min = data['tmp_min']  # 最低温度
            sr = data['sr']  # 日出时间
            ss = data['ss']  # 日落时间
            Data = {

                'date': date,
                'cond': cond,
                'max': max,
                'min': min,
                'sr': sr,
                'ss': ss,
                'city': city,
                'province': province,
            }
            datas.append(Data)
        print(datas[0])
        self.text = "%s日份天气预报到账啦\n今天%s的天气情况为%s\n最高温度%s℃，最低温度%s℃\n太阳公公出来的时间大约是%s,太阳公公落下的时间大约是%s请注意合理安排时间进行学习,娱乐,锻炼。\n今天的天气预报到此,祝您有个愉快的一天" % (
            self.today_time, Data['city'], Data['cond'], Data['max'], Data['min'], Data['sr'], Data['ss'])
        return self.text


if __name__ == '__main__':
    for i in range(0, 1):
        time.sleep(3)
        send = weater_demo()
        text = send.get_weather_data()
        print(text)
