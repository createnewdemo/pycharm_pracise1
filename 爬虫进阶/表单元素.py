# 常见表单元素 ： input type='text/password/emil/number'
# button , input[type='submit']
# checkbox: input='checkbox'
# select:下拉列表
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 操作输入框
# driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)#可以使用driver操作浏览器了
# driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
#
# inputTag.send_keys('python')
# time.sleep(3)
#

# 操作checkbox
# driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)#可以使用driver操作浏览器了
# driver.get('https://www.douban.com/')
# try:
#     remember_Btn = driver.find_element_by_name("remember")
#     remember_Btn.click()
# except:
#     time.sleep(2)
#     driver.close()


# 操作select标签
driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)  # 可以使用driver操作浏览器了
driver.get('https://www.baidu.com/')
try:
    input_tag = driver.find_element_by_id("kw")
    input_tag.send_keys('python')
    remember_Btn = driver.find_element_by_id("su")
    remember_Btn.click()
    time.sleep(5)
    driver.close()
except:
    print("失败了")
    time.sleep(2)
    driver.close()
