# encoding: utf-8
# -*- coding: gbk -*-
# !/usr/bin/env python3
from selenium import webdriver  # line:1
import time  # line:2
import winsound  # line:3

option = webdriver.ChromeOptions()  # line:5
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # line:6
browser = webdriver.Chrome(executable_path="E:\pycharm\chromediver\chromedriver.exe")  # line:7
WIDTH = 320  # line:8
HEIGHT = 640  # line:9
PIXEL_RATIO = 3.0  # line:10
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'  # line:11
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                   "userAgent": UA}  # line:14
options = webdriver.ChromeOptions()  # line:15
options.add_experimental_option('mobileEmulation', mobileEmulation)  # line:16
drive = webdriver.Chrome(executable_path="E:\pycharm\chromediver\chromedriver.exe")  # line:17
times = 0  # line:18
url = 'https://detail.tmall.com/item.htm?id=601209237183'


def monphone(url):  # line:19
    global times  # line:20
    drive.get(url)  # line:21
    i = drive.find_element_by_xpath('//*[@id="s-actionBar-container"]/div/div[2]/a[3]').text  # line:22
    print(i)  # line:23
    times = times + 1  # line:24
    return i  # line:25


def login():  # line:27
    browser.get("https://www.taobao.com")  # line:29
    time.sleep(3)  # line:30
    if browser.find_element_by_link_text("亲，请登录"):  # line:31
        browser.find_element_by_link_text("亲，请登录").click()  # line:32
        print(f"请尽快扫码登录")  # line:33
        time.sleep(10)  # line:34


def mon(OO0OO00OOOOO0000O):  # line:37
    browser.get(OO0OO00OOOOO0000O)  # line:38
    global state  # line:39
    OO0OOO0O00O000OOO = '''Object.defineProperties(navigator,{webdriver:{get:() => false}}) '''  # line:40
    OO00OOO0O0OOOOO00 = '''window.navigator.chrome = {runtime:{}, };'''  # line:41
    OO0OO000O00OOO0OO = '''Object.defineProperty(navigator, 'languages',{get: () => ['en-US', 'en']}); '''  # line:42
    O0O0O0OOO000O0OO0 = '''Object.defineProperty(navigator, 'plugins',{get:() => [1, 2, 3, 4, 5,6],}); '''  # line:43
    browser.execute_script(OO0OOO0O00O000OOO)  # line:44
    browser.execute_script(OO00OOO0O0OOOOO00)  # line:45
    browser.execute_script(OO0OO000O00OOO0OO)  # line:46
    browser.execute_script(O0O0O0OOO000O0OO0)  # line:47
    time.sleep(3)  # line:48
    try:  # line:49
        OO00OOOOO0O00OOO0 = browser.find_element_by_id("J_EmStock").text  # line:50
        print(OO00OOOOO0O00OOO0)  # line:51
        state = 1  # line:52
    except:  # line:53
        print(f'没有找到库存信息')  # line:54
        state = 0  # line:55


def clear():  # line:57
    drive.delete_all_cookies()  # line:58
    global times  # line:59
    times = 0  # line:60
    print("已清除缓冲区")  # line:61


def choice(O0O000OO0OOO0OOOO):  # line:63
    OOO0O000OOOO00OO0 = browser.page_source  # line:64
    if "已选择" in OOO0O000OOOO00OO0:  # line:65
        print('已选择')  # line:66
        return 1  # line:67
    else:  # line:68
        print('没有发现选中目标')  # line:69
        browser.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[' + str(
            O0O000OO0OOO0OOOO) + ']').click()  # line:71


def buy():  # line:73
    O00000O00O0O00000 = 0  # line:74
    while O00000O00O0O00000 < 15:  # line:75
        try:  # line:76
            print(f'类型寻找中' + str(O00000O00O0O00000))  # line:77
            OO0OO0OO00OOO00O0 = browser.find_element_by_xpath(
                '//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[' + str(
                    O00000O00O0O00000) + ']').text  # line:79
            print(f'选择类型')  # line:80
            browser.find_element_by_xpath(
                '//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[' + str(
                    O00000O00O0O00000) + ']').click()  # line:82
            choice(O00000O00O0O00000)  # line:83
            OO00OO00000OOOO0O = browser.find_element_by_id("J_EmStock").text  # line:84
            print(OO00OO00000OOOO0O)  # line:85
            print(OO0OO0OO00OOO00O0)  # line:86
            browser.find_element_by_id("J_LinkBuy").click()  # line:87
            time.sleep(1)  # line:88
            browser.find_element_by_class_name("go-btn").click()  # line:89
            winsound.Beep(500, 2000)  # line:90
            return 1  # line:91

            break  # line:92
        except:  # line:93
            O00000O00O0O00000 = O00000O00O0O00000 + 1  # line:94
            print(O00000O00O0O00000)  # line:95


login()  # line:100
url = input()  # line:101
while True:  # line:102
    state = monphone(url)  # line:103
    if times >= 100:  # line:104
        clear()  # line:105
    if state == "立即购买":  # line:106
        mon(url)  # line:107
        if state == 1:  # line:108
            success = buy()  # line:109
            if success == 1:  # line:110
                print('成功')  # line:111
                winsound.Beep(500, 2000)  # line:112
                break  # line:113
