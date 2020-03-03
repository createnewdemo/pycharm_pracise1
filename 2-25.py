# -*- coding: gbk -*-
from selenium import webdriver
import re
import time

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
url = 'https://www.landchina.com/default.aspx?tabid=261&ComName=default'
driver.get(url)
time.sleep(3)
# js = 'window.open("{}");'.format("https://www.sogou.com")
# driver.execute_script(js)
# #driver.switch_to.window(driver.window_handles[1])
# handles = driver.window_handles
# print(handles)
# for handle in handles:
#     if handle != driver.current_window_handle:
#         print('switch',handle)
#         driver.switch_to.window(handle)
# driver.close()


# numbers = driver.find_element_by_xpath("//tr/td[@class='pager']")
# number = numbers.text
# num = re.findall(r'共(\d+)页',number)[0]
# print(num)

times = driver.find_element_by_id("TAB_QueryConditionItem268").click()

time1 = driver.find_element_by_id("TAB_queryDateItem_268_1").send_keys("2020-1-1")
time.sleep(2)
time2 = driver.find_element_by_id("TAB_queryDateItem_268_2").send_keys("2020-1-30")
time.sleep(5)
check = driver.find_element_by_id("TAB_QueryButtonControl")
time.sleep(2)
driver.execute_script('arguments[0].click();', check)

# time.sleep(2)
# aElements = driver.find_element_by_id("TAB_QueryConditionItem227").click()
# time.sleep(2)
aElements = driver.find_elements_by_tag_name("a")
time.sleep(2)
names = []
for name in aElements:
    if (name.get_attribute("href") is not None and "javascript:void" in name.get_attribute("href")):
        names.append(name)
print(names)
time.sleep(2)
driver.execute_script('arguments[0].click();', names[-2])
js = "var q=document.getElementById('id').scrollTop=10000"
driver.execute_script(js)
a = 1
u = 'F:\\pycharm_pracise\\land\\Picture\\%s.png' % a
picture_url = driver.get_screenshot_as_file(u)
# print(searchBtn)
# searchBtn.click()


# aElements = driver.find_elements_by_tag_name("a")
# print(1)
# for name in aElements:
#     if(name.get_attribute("href") is not None and "javascript:void" in name.get_attribute("href")):
#         print(name)
#         time.sleep(5)
#         driver.execute_script('arguments[0].click();', name)
#         time.sleep(5)
# name.click()
#         print("jies")
#         name=name.get_attribute('href')
#         print(name)
#         #name.click()


# print(name)
# time.sleep(1)
# driver.get('https://www.baidu.com/s?ie=utf-8&tn=02003390_22_hao_pg&wd=ip')
