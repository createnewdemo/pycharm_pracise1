import requests
from lxml import etree
import csv
import random
import pandas as pd
import json
import jsonpath
from selenium import webdriver

requests.packages.urllib3.disable_warnings()
import time
import os


def drop_down(url):
    driver.get(url)
    infos = []
    time.sleep(1)
    driver.maximize_window()
    size = driver.get_window_size()
    het = size['height']
    xiala = het // 50 * 50 - 100
    dayin = driver.find_element_by_xpath('//*[@id="btnPrint"]')
    gaodu = (dayin.location)['y']
    cishu = gaodu // xiala + 1
    title = driver.find_element_by_xpath('//*[@id="lblTitle"]').text
    data = {
        '1': url,
        '2': title
    }
    infos.append(data)
    aaa = pd.DataFrame.from_dict(infos)
    aaa.to_csv('已截图.csv', mode='a', encoding='utf-8-sig', header=False, index=False)
    for i in range(0, cishu):
        js = 'window.scrollTo(0,%s)' % (i * xiala)
        driver.execute_script(js)
        time.sleep(2)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        isExists = os.path.exists('C:\\Users\\lixiang\\PycharmProjects\\untitled\\' + title)
        if not isExists:
            os.makedirs('C:\\Users\\lixiang\\PycharmProjects\\untitled\\' + title)
        jietu = driver.get_screenshot_as_file(
            'C:\\Users\\lixiang\\PycharmProjects\\untitled\\' + title + '\\' + title + picture_time + '.png')
    time.sleep(1)


def main():
    f1 = open(r'muluye.csv', 'r', encoding='utf-8')
    # f2 = open(r'已截图.csv', 'r', encoding='utf-8')
    csvreader1 = csv.reader(f1)
    # csvreader2 = csv.reader(f2)
    columns1 = [column[0] for column in csvreader1]
    # columns2 = [column[0] for column in csvreader2]
    urls = []
    columns1_qc = list(set(columns1))
    columns1_qc.sort(key=columns1.index)
    print(len(columns1_qc))
    for column in columns1_qc:
        # if column not in columns2:
        urls.append(column)
    print(len(urls))
    for url in urls[1:13]:
        drop_down(url)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get(
        'https://www.landchina.com//DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&recorderguid=JYXT_ZJGG_12374&sitePath=')
    driver.implicitly_wait(8)
    main()
