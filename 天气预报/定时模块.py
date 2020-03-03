# -*- coding: utf-8 -*-
import datetime
import threading


class time_send(object):
    def time_send(self):
        timer = threading.Timer(86400, self.func)
        timer.start()
        # city = '信阳'
        # text = self.get_weatherinfo(city)
        # self.wx.send_text(to_user='LW98118', msg=text)
        print('到时间了')

    def func(self):
        # now_time = datetime.datetime.now()
        # # 获取明天时间
        # next_time = now_time + datetime.timedelta(days=+1)
        # next_year = next_time.date().year
        # next_month = next_time.date().month
        # next_day = next_time.date().day
        # # print(now_time,next_time,next_year,next_month,next_day)
        # # 获取明天7点时间
        # next_time = datetime.datetime.strptime(
        #     str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 07:00:00", "%Y-%m-%d %H:%M:%S")
        # # 获取距离明天7点时间，单位为秒
        # timer_start_time = (next_time - now_time).total_seconds()
        print('执行到这了')
        # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
        timer = threading.Timer(10, self.time_send)
        timer.start()


if __name__ == '__main__':
    send = time_send()
    send.func()
