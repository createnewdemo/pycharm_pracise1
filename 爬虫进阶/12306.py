from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random


class Qiaopiao(object):

    def __init__(self):  # 属性
        self.login_url = "https://kyfw.12306.cn/otn/login/init"
        self.driver = webdriver.Chrome(executable_path="E:\pycharm\chromediver\chromedriver.exe")
        self.initmy_url = "https://kyfw.12306.cn/otn/view/index.html"
        self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.passenger_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'

    def login(self):
        print("请先自己登录账号")
        self.driver.get(self.login_url)
        time.sleep(1)
        self.driver.find_element_by_id('username').send_keys("17190199811")
        time.sleep(1)
        self.driver.find_element_by_id('password').send_keys("lsl723723")
        print("手动验证图像验证码谢谢合作")
        WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.initmy_url))  # 等待
        print("登陆成功")

    def wait_input(self):
        self.from_station = "北京"
        self.to_station = "上海"
        self.depart_time = "2020-02-14"
        self.passengers = "李世林"  # 用逗号分割成一个列表
        self.strains = "G153"
        # self.from_station = input("出发地：")
        # self.to_station = input("目的地：")
        # self.depart_time = input("出发时间（格式****-**-**）：")
        # self.passengers = input("乘客姓名（如有多个乘客用英文逗号隔开）：").split(",")#用逗号分割成一个列表
        # self.strains = input("车次（如有多个乘客用英文逗号隔开）：").split(",")

    def order_ticket(self):
        try:
            # 跳转到查票的界面
            self.driver.get(self.search_url)
            # 等待出发地输入是否正确
            WebDriverWait(self.driver, 1000).until(
                EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station)
                )  # 注意函数EC.text_to_be_present_in_element_value里面参数是个元组
            # 等待目的地输入是否正确
            WebDriverWait(self.driver, 1000).until(
                EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
                )
            # 等待出发日期输入是否正确
            WebDriverWait(self.driver, 1000).until(
                EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
                )
            # 等待查询按钮是否可用
            WebDriverWait(self.driver, 1000).until(EC.element_to_be_clickable((By.ID, "query_ticket"))
                                                   )
            # 如果能被点击了，那么就找到查询按钮，执行点击事件
            searchBtn = self.driver.find_element_by_id("query_ticket")
            searchBtn.click()

            # 点击了查询按钮以后，等待车次信息是否显示
            WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))

            )
            # 找到所有没有datatran属性的tr标签，这些是存储了车次信息的
            tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
            # 遍历所有满足条件的tr标签
            for tr in tr_list:
                train_number = tr.find_element_by_class_name("number").text
                # print(train_number)
                # print('='*30)
                if train_number in self.strains:
                    left_ticket = tr.find_element_by_xpath(".//td[4]").text
                    count = 1
                    while left_ticket == '无' or left_ticket == '--' or left_ticket == '候补':
                        print("暂无余票,正在尝试第%s次抢票···" % count)
                        time.sleep(1)
                        # time.sleep(random.randint(300, 1000))
                        searchBtn.click()
                        count += 1
                    if left_ticket == "有" or left_ticket.isdigit:
                        orderBtn = tr.find_element_by_class_name('btn72')
                        orderBtn.click()

                        # 等待是否确认来到确认乘客的页面
                        WebDriverWait(self.driver, 1000).until(
                            EC.url_to_be(self.passenger_url)
                        )
                        time.sleep(1)
                        """
                        
                        try {
                WebElement element=driver.findElement(By.xpath("//input[@id='name']"));
                element.sendKeys("输入的文本");
            }
            catch(org.openqa.selenium.StaleElementReferenceException ex)
            {
                WebElement element=driver.findElement(By.xpath("//input[@id='name']"));
                element.sendKeys("输入的文本");
            }
                        """
                        WebDriverWait(self.driver, 1000).until(
                            EC.presence_of_element_located(
                                (By.XPATH, ".//ul[@id = 'normal_passenger_id']/li")))  # 定位到以后在操作
                        passanger_labels = self.driver.find_elements_by_xpath(
                            ".//ul[@id = 'normal_passenger_id']/li/label")
                        for passanger_label in passanger_labels:
                            name = passanger_label.text
                            if name in self.passengers:
                                # time.sleep(1)
                                passanger_label.click()
                        submit_Btn = self.driver.find_element_by_id("submitOrder_id")
                        # time.sleep(1)
                        submit_Btn.click()
                        # self.driver.switch_to.frame(self.driver.find_element_by_class_name("dhx_modal_cover_ifr"))

                        # WebDriverWait(self,1000).until(EC.presence_of_element_located((By.XPATH,".//div[@class='dhtmlx_wins_body_outer']")))
                        # qr_submit_Btn = self.driver.find_element_by_id("qr_submit_id")
                        # qr_submit_Btn.click()
                        time.sleep(2)
                        self.driver.find_element_by_id("qr_submit_id").click()
                        time.sleep(5)
                        print("已经抢到票，请喝杯茶再来付款")
                        print("系统正常退出……")
                        exit()
        except:
            print("应该完成了吧。。")

            # passenger_name_lists = self.driver.find_elements_by_xpath("//*[@id='normal_passenger_id']/li/label")
            # print(passenger_name_lists)
            # for passenger_name_list in passenger_name_lists:
            #     print(passenger_name_lists+'2')
            #
            #
            #     passenger_name = passenger_name_list.find_element_by_xpath(".//ul//label").text
            #     if passenger_name in self.passengers:
            #         passenger_Btn = passenger_name_list.find_element_by_xpath(".//ul//label")
            #         passenger_Btn.click()
            #         print(passenger_name)

    def run(self):
        self.wait_input()  # 先让用户给信息输入完成

        self.login()
        self.order_ticket()


if __name__ == '__main__':
    spider = Qiaopiao()
    spider.run()
