from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.douban.com/')
elementi = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_toframe(elementi)

# driver.implicitly_wait(10)

driver.switch_to.frame()
Element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'phone'))
)
print(Element)

# sreach_window=driver.current_window_handle
# Tag = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/p[2]/label')
# Tag.click()
