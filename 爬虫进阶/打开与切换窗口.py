from selenium import webdriver
import time

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)  # 可以使用driver操作浏览器了
driver.get('https://www.baidu.com/')
time.sleep(2)
driver.execute_script("window.open('http://www.douban.com/')")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
time.sleep(2)
