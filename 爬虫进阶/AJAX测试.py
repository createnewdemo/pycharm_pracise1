from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)  # 可以使用driver操作浏览器了
driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag = driver.find_elements(By.CSS_SELECTOR, ".quickdelete-wrap > input")[0]  # 返回的是列表

inputTag.send_keys('python')

# print(driver.page_source)
# time.sleep(5)
# driver.quit()
