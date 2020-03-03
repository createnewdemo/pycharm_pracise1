# -*- coding: gbk -*-
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    # 设置邮箱的域名
    HOST = 'smtp.qq.com'
    # 设置邮件标题
    SUBJECT = '黑马资源'
    # 设置发件人邮箱
    FROM = '320783214@qq.com'
    # 设置收件人邮箱
    TO = '359724828@qq.com'  # 可以填写多个邮箱，用逗号分隔，后面会用split做逗号分割
    message = MIMEMultipart('related')
    # --------------------------------------发送文本-----------------
    # 发送邮件正文到对方的邮箱中
    text = '链接：https://pan.baidu.com/s/1GMcZ38OlYa-NN7hlDLUszg 提取码：n75H '
    message_html = MIMEText(text, 'plain', 'utf-8')  # \n为换行
    message.attach(message_html)

    # -------------------------------------添加文件---------------------
    # 要确定当前目录有test.csv这个文件
    # message_xlsx = MIMEText(open('today_weather.xls', 'rb').read(), 'base64', 'utf-8')
    # 设置文件在附件当中的名字
    # message_xlsx['Content-Disposition'] = 'attachment;filename="today_weather.xls"'
    # message.attach(message_xlsx)

    # 设置邮件发件人
    message['From'] = FROM
    # 设置邮件收件人
    message['To'] = TO
    # 设置邮件标题
    message['Subject'] = SUBJECT

    # 获取简单邮件传输协议的证书
    email_client = smtplib.SMTP_SSL(host='smtp.qq.com')
    # 设置发件人邮箱的域名和端口，端口为465
    email_client.connect(HOST, '465')
    # ---------------------------邮箱授权码------------------------------
    result = email_client.login(FROM, 'vazakcfvsmgnbhif')
    print('登录结果', result)

    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
    # 关闭邮件发送客户端
    email_client.close()
    print('发送成功')


send_email()
