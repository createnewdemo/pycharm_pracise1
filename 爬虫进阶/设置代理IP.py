from selenium import webdriver

driver_path = r'E:\pycharm\chromediver\chromedriver.exe'

options = webdriver.ChromeOptions()

options.add_argument("--proxy-server=http://118.212.105.64:9999")

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.get('https://www.baidu.com/s?ie=utf-8&tn=02003390_22_hao_pg&wd=ip')
