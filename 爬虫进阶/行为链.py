# 行为链：
# 有时候在页面中的操作可能要有很多步，那么这时候可以使用鼠标行为链类ActionChains来完成。比如现在要将鼠标移动到某个元素上并执行点击事件。那么示例代码如下：
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)  # 可以使用driver操作浏览器了
driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')
# 行为链
actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()
