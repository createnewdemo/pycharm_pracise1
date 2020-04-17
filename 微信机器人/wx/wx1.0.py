from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
# -*- coding: gbk -*-
import random
import os
import requests
import threading
import datetime


class wx_robot(object):
    def __init__(self):

        self.wx = WechatPCAPI(on_message=self.on_message, log=logging)
        self.wx.start_wechat(block=True)
        print('这里执行了没1')
        logging.basicConfig(level=logging.INFO)
        self.queue_recved_message = Queue()
        while not self.wx.get_myself():
            time.sleep(1)
            print(self.wx.get_myself())
            # print('这里执行了没1')
            # wx.send_text(to_user='friends', msg='登陆成功')
            time.sleep(1)
        print('登陆成功')

    def on_message(self, message):
        self.queue_recved_message.put(message)

    # def get_messages(self):
    #     while True:
    #         message = self.queue_recved_message.get()
    #         print('0')
    #         print(message)
    def get_msg_content(self):  # 信息消息
        while True:
            time.sleep(1)
            message = self.queue_recved_message.get()
            print(message)
            if 'msg' in message.get('type'):
                # print('2')
                # 这里是判断收到的是消息 不是别的响应
                msg_content = message.get('data', {}).get('msgcontent', '')
                print(msg_content)
                # text = self.get_weatherinfo(city)
                send_or_recv = message.get('data', {}).get('is_recv', '')  # 判断为接收消息的变量
                print(send_or_recv)
                self.wx_id = message.get('data', {}).get('msgfromid', '')  # 目标wxID

                if 'sysmsg type' in msg_content:
                    continue
                elif '1' == msg_content:
                    time.sleep(1)
                    tishi = '现有功能：\n输入命令：天气+城市\n输入命令：b站小视频\n输入命令：每日一句\n输入命令：主人博客\n输入命令：翻译+文本\n输入命令：每日壁纸\n输入命令：新冠数据\n输入命令：历史上的今天'
                    self.wx.send_text(to_user=self.wx_id, msg=tishi)
                if msg_content == '新冠数据':
                    try:
                        time.sleep(1)
                        info = self.COV()
                        text = '现存确诊:' + str(info[0]) + '\n较昨日增加:' + str(info[1]) + '人' + '\n现存疑似:' + str(
                            info[2]) + '人' + '\n疑似增加:' + str(info[3]) + '人' + '\n累计治愈:' + str(
                            info[4]) + '人' + '\n更新时间:' + str(info[5])
                        self.wx.send_text(to_user=self.wx_id, msg=text)
                    except Exception as error:
                        print(error)
                if '壁纸' in msg_content:
                    try:
                        time.sleep(1)
                        self.bz()
                        self.wx.send_img(to_user=self.wx_id, img_abspath=r'C:\Users\Administrator\Desktop\wx-BO\bz.jpg')
                    except Exception as error:
                        print(error)
                if msg_content == '主人博客':
                    time.sleep(1)
                    self.wx.send_link_card(
                        to_user=self.wx_id,
                        title='博客',
                        desc='我的博客',
                        target_url='http://101.133.237.148:8001/',
                        img_url='http://101.133.237.148:8001/usr/uploads/2020/02/2030670353.jpg'
                    )
                if '翻译+' in msg_content:
                    try:
                        time.sleep(1)
                        text = msg_content.split('+')[-1]
                        text = self.translation(text)
                        self.wx.send_text(to_user=self.wx_id, msg=text)
                    except Exception as error:
                        print(error)
                if msg_content == '历史上的今天':
                    try:
                        time.sleep(1)
                        info = self.history()

                        self.wx.send_text(to_user=self.wx_id, msg=info)
                    except Exception as error:
                        print(error)
                if msg_content == '每日一句':
                    try:
                        time.sleep(1)
                        eng = self.get_news()[0]
                        cn = self.get_news()[1]
                        self.wx.send_text(to_user=self.wx_id, msg=eng)
                        self.wx.send_text(to_user=self.wx_id, msg=cn)
                    except Exception as error:
                        print(error)
                if msg_content == 'b站小视频':
                    try:
                        time.sleep(1)
                        url = self.get_url()
                        print(url)
                        self.wx.send_text(to_user=self.wx_id, msg=url)
                    except Exception as error:
                        print(error)
                city = msg_content.split('+')[-1]
                if msg_content == '天气' + '+' + city:
                    try:
                        time.sleep(1)
                        text = self.get_weatherinfo(city)
                        print('执行到这里了----')
                        self.wx.send_text(to_user=self.wx_id, msg=text)
                    except Exception as error:
                        print(error)

    def COV(self):
        url = 'https://api.yonyoucloud.com/apis/dst/ncov/country'
        Headers = {
            'apicode': '1aaef2983911441ba03470a297b1c163'
        }
        r = requests.get(url, headers=Headers).json()
        currentConfirmedCount = r['data']['currentConfirmedCount']  # 现存确诊（去掉已经治愈）
        currentConfirmedAdd = r['data']['currentConfirmedAdd']  # 较昨日增加或减少
        suspectedCount = r['data']['suspectedCount']  # 现存疑似
        suspectedAdd = r['data']['suspectedAdd']  # 疑似增加
        curedCount = r['data']['curedCount']  # 累计治愈
        updateTime = r['data']['updateTime']  # 更新时间
        # print(updateTime)
        info = [currentConfirmedCount, currentConfirmedAdd, suspectedCount, suspectedAdd, curedCount, updateTime,
                updateTime]
        return info

    def history(self):
        url = 'http://api.63code.com/history/api.php?format=json'
        while True:
            try:
                r = requests.get(url)
                contents = r.json()['content']
                # print(contents)
                contents = "\n".join(str(i) for i in contents)
                return contents
                break
            except:
                continue

    def bz(self):  # 壁纸
        url = 'http://api.63code.com/bing/api.php'
        r = requests.get(url)
        with open('bz.jpg', 'wb') as f:
            f.write(r.content)

        """
        翻译功能
        """

    def translation(self, text):
        # text = '翻译'
        url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}'.format(text)
        r = requests.get(url).json()
        result = r['translateResult'][0][0]['tgt']
        return result

    """
    每日一句
    """

    def get_news(self):
        # 这里是把今日糍粑每日一句中拿过来的信息发送给你朋友
        url = "http://open.iciba.com/dsapi/"
        r = requests.get(url)
        contents = r.json()['content']
        translation = r.json()['note']
        print(contents)
        print(translation)
        return contents, translation

    """
    发送定时消息
    """

    def time_send(self):
        timer = threading.Timer(86400, self.func)
        timer.start()
        eng = self.get_news()[0]
        cn = self.get_news()[1]
        city = '信阳'
        text = self.get_weatherinfo(city)
        self.wx.send_text(to_user='wxid_6xvxonr3o8m522', msg='早安')
        time.sleep(1)
        self.wx.send_text(to_user='wxid_6xvxonr3o8m522', msg=text)
        time.sleep(1)
        self.wx.send_text(to_user='wxid_6xvxonr3o8m522', msg=eng)
        time.sleep(1)
        self.wx.send_text(to_user='wxid_6xvxonr3o8m522', msg=cn)
        time.sleep(1)

    """
    #设置定时
    """

    def func(self):
        now_time = datetime.datetime.now()
        # 获取明天时间
        next_time = now_time + datetime.timedelta(days=+1)
        next_year = next_time.date().year
        next_month = next_time.date().month
        next_day = next_time.date().day
        # print(now_time,next_time,next_year,next_month,next_day)
        # 获取明天7点时间
        next_time = datetime.datetime.strptime(
            str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 07:30:00", "%Y-%m-%d %H:%M:%S")
        # 获取距离明天7点时间，单位为秒
        timer_start_time = (next_time - now_time).total_seconds()
        print(timer_start_time)
        # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
        timer = threading.Timer(timer_start_time, self.time_send)
        timer.start()

    """
    天气信息
    """

    def get_weatherinfo(self, city):
        try:
            url = 'https://free-api.heweather.net/s6/weather/forecast?location={}&key=3f8659a2ab674ca6bdc3e740462a6ae1'.format(
                city)
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
            self.text = "今天%s的天气情况为%s\n最高温度%s℃，最低温度%s℃\n请注意合理安排时间进行学习,娱乐,锻炼。\n祝您有个愉快的一天" % (
            Data['city'], Data['cond'], Data['max'], Data['min'])
            return self.text
        except:
            print('输入错误')
            self.wx.send_text(to_user=self.wx_id, msg='猪啊，让你输入格式为；天气+你的城市')  # 天气现象

    """
    小视频链接
    """

    def get_url(self):
        user_agent = [
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
        try:
            headers = {
                'User-Agent': random.choice(user_agent),
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'http://vc.bilibili.com/p/eden/rank'
            }
            params = {
                'page_size': 10,
                'next_offset': '',
                'tag': '今日热门',
                'platform': 'pc'
            }

            try:
                url = 'https://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
                html = requests.get(url, params=params, headers=headers)
                r = html.json()
                infos = r['data']['items']
                info = infos[0]
                url = info['item']['video_playurl']
                print(url)
                return url
            except:
                print('error')
        except:
            print('error')
    # friends = wx.get_friends()
    # print(friends)
    # wx.send_link_card(
    #     to_user= friends,
    #     title='博客',
    #     desc='我的博客',
    #     target_url='http://101.133.237.148:8001/',
    #     img_url='http://101.133.237.148:8001/usr/uploads/2020/02/4020504396.png'
    # )


def main():
    return_massage = wx_robot()
    # t1 = threading.Thread(target=return_massage.time_send)
    return_massage.func()  # 先启用闹钟
    return_massage.get_msg_content()

    # t2 = threading.Thread(target=return_massage.get_msg_content)


main()
