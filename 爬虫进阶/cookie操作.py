from selenium import webdriver
import time

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
for cookie in driver.get_cookies():
    print(cookie)
print('=' * 30)
print(driver.get_cookie("BD_HOME"))
print('=' * 30)
driver.delete_cookie("BD_HOME")
print(driver.get_cookie("BD_HOME"))
driver.delete_all_cookies()
