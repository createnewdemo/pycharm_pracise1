# encoding: utf-8
import time
from selenium import webdriver
from lxml import etree
import pymysql

index = 0


class LagouSpider(object):
    driver_path = r'E:\pycharm\chromediver\chromedriver.exe'

    def __init__(self):  # 类中变量
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.position = []

    def parse_list_page(self, source):  # 解析页面中的每个职位链接 调用self.request_detail_page(link)函数解析
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for index, link in enumerate(links):
            print("=============正在爬取第%d条职位信息=========" % (index + 1))
            self.request_detail_page(link)
            # print("=============爬取第%d条职位信息=========" % index)
            time.sleep(2)

    def request_detail_page(self, url):  # 解析出职位的信息url 并调用下一个函数拿出信息
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self, source):  # 解析详细信息处理
        html = etree.HTML(source)
        time.sleep(5)
        position_name = html.xpath("//div[@class='job-name']//h1[@class='name']/text()")
        position_salary = html.xpath("//dd[@class='job_request']//h3//span[@class='salary']/text()")[
            0].strip()  # 列表  要获取里面的文本还要加text（）加了就不是列表了
        # print(position_salary)
        # position_salary = position_request_spans[0].xpath('.//text()')[0].strip()#里面存的还是Element span 还可以xpath解析
        position_city = html.xpath("//dd[@class='job_request']//h3//span[2]/text()")[0].replace('/', '').strip()
        position_experience = html.xpath("//dd[@class='job_request']//h3//span[3]/text()")[0].replace('/', '').strip()
        educational_background = html.xpath("//dd[@class='job_request']//h3//span[4]/text()")[0].replace('/',
                                                                                                         '').strip()
        position_form = html.xpath("//dd[@class='job_request']//h3//span[5]/text()")[0].replace('/', '').strip()
        job_detail = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        position = {
            'name': position_name,
            'salary': position_salary,
            'city': position_city,
            'experience': position_experience,
            'educational': educational_background,
            'form': position_form,
            'job_detail': job_detail
        }
        self.position.append(position)
        print(position)
        # self.mysql(position)
        try:
            self.mysql(position)
            print('=' * 30 + "写入数据库成功" + '=' * 30)
        except Exception as result:
            print('=' * 30 + '写入数据库失败原因是%s' % result + '=' * 30)

    def mysql(self, position):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='py_mysql_demo', port=3306)
        cursor = conn.cursor()
        sql = """
        insert into position_demo(id,position_name,position_salary,position_city,position_experience,position_form,job_detail) values(null,%s,%s,%s,%s,%s,%s)
        """
        position = (position['name'], position['salary'], position['city'], position['experience'], position['form'],
                    position['job_detail'])
        cursor.execute(sql, position)
        conn.commit()
        conn.close()

    def switch_page(self):
        self.driver.execute_script("window.open('" + self.url + "')")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # html_page = etree.HTML(source)
        time.sleep(3)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        where = self.driver.find_element_by_xpath("/html/body/div[8]/div/div[2]")
        where.click()
        time.sleep(2)
        Btn = self.driver.find_element_by_xpath("//*[@id='s_position_list']/div[2]/div/span[6]")
        Btn.click()
        time.sleep(3)
        new_source = self.driver.page_source  # 获取source
        return new_source

    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source  # 获取source
        self.parse_list_page(source)
        try:
            while True:
                source = self.switch_page()
                time.sleep(3)
                self.parse_list_page(source)
                time.sleep(3)

        except Exception as result:

            print(result)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
