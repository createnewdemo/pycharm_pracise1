from selenium import webdriver

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)  # 可以使用driver操作浏览器了
driver.get('https://www.douban.com/')
driver.implicitly_wait(10)
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
# driver.switch_to.frame("frame1")  # 2.用id来定位
# driver.switch_to.frame("myframe")  # 3.用name来定位
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe'))
tag = driver.find_element_by_xpath('//*[@id="account-form-remember"]')
tag.click()
print(tag)
