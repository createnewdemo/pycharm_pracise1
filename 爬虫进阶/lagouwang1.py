import requests
from lxml import etree
import time
import pymysql

headers = {
    'Connection': 'keep-alive',
    'X-Anit-Forge-Code': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Sec-Fetch-Dest': 'empty',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token': 'None',
    'Origin': 'https://www.lagou.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie':'user_trace_token=20200208193510-5586a31f-007f-45b8-bb4d-99a5aac759f7; _ga=GA1.2.2085922697.1581161713; LGUID=20200208193511-3368313c-615b-4ea7-9d9d-b9dc7c2dcdf1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217024954435287-0de7e370d91e82-b791b36-2073600-170249544369e1%22%2C%22%24device_id%22%3A%2217024954435287-0de7e370d91e82-b791b36-2073600-170249544369e1%22%7D; sajssdk_2015_cross_new_user=1; _gid=GA1.2.1525120981.1581161727; gate_login_token=a873c73c32034cdb02930451b7178f17ec571fac318e988021abc01251b5f354; LG_LOGIN_USER_ID=3152818b73e5c9620be749df93a9e64952a92e574d420cdecfe0bb7ed4ffa32c; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; lagou_utm_source=B; WEBTJ-ID=20200208234528-170257a2d84454-0fa4c5e5b726a4-b791b36-2073600-170257a2d85365; JSESSIONID=ABAAABAABFIAAACF53CAC57345904E69B50323CF63E5EDD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581161712,1581176729; _putrc=81CB94937CE62F51123F89F2B170EADC; login=true; unick=%E6%9D%8E%E4%B8%96%E6%9E%97; LGSID=20200208234528-9c48b496-c4dc-4b98-adfe-ec80662a28da; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5Fpython%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F6793277.html%3Fshow%3Dd69f941fca0b4c419e405f84f275dd05; X_HTTP_TOKEN=965ebd8085b5ec291237711851a051ab0395650a4d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581177322; TG-TRACK-CODE=search_code; LGRID=20200208235852-d6ab7cb3-d7f7-4cfc-9ea7-8b3fa832258a; SEARCH_ID=a71f4335b9e4499088aac363b6805f71'
}


def request_list_page():
    s = requests.Session()
    first_url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first': 'false',
        'pn': '1',
        'kd': 'python'
    }
    for x in range(1, 3):
        data['pn'] = x
        s.get(url=first_url, headers=headers, timeout=4)
        cookings = s.cookies
        r = s.post(url=url, headers=headers, data=data, cookies=cookings, timeout=3)
        time.sleep(3)
        result = r.json()
        # print(result)
        positions = result['content']['positionResult']['result']
        # print(positions)
        print('正在爬取第%d页' % x)
        for position in positions:
            positionID = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html?show=d69f941fca0b4c419e405f84f275dd05' % positionID
            parse_position_url(position_url)
            time.sleep(3)
            for a in range(1, 100):
                print('正在爬取第%d个职位' % x)


def parse_position_url(url):
    r = requests.post(url, headers=headers)
    r.encoding = 'utf-8'
    r = r.text
    html = etree.HTML(r)
    time.sleep(3)
    position_name = html.xpath("//div[@class='job-name']//h1[@class='name']/text()")
    position_salary = html.xpath("//dd[@class='job_request']//h3//span[@class='salary']/text()")[
        0].strip()  # 列表  要获取里面的文本还要加text（）加了就不是列表了
    print(position_salary)
    # position_salary = position_request_spans[0].xpath('.//text()')[0].strip()#里面存的还是Element span 还可以xpath解析
    position_city = html.xpath("//dd[@class='job_request']//h3//span[2]/text()")[0].replace('/', '').strip()
    position_experience = html.xpath("//dd[@class='job_request']//h3//span[3]/text()")[0].replace('/', '').strip()
    educational_background = html.xpath("//dd[@class='job_request']//h3//span[4]/text()")[0].replace('/', '').strip()
    position_form = html.xpath("//dd[@class='job_request']//h3//span[5]/text()")[0].replace('/', '').strip()
    job_detail = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    # print(job_detail)
    # print(position_request_spans)
    conn = pymysql.connect(host='localhost', user='root', password='root', database='py_mysql_demo', port=3306)
    cursor = conn.cursor()
    sql = """
    insert into position_demo(id,position_name,position_salary,position_city,position_experience,position_form,job_detail) values(null,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql, (position_name, position_salary, position_city, position_experience, position_form, job_detail))
    conn.commit()
    conn.close()

    # print(r.json())#json方法，如果是json数据，自动load返回来的是个字典


def main():
    request_list_page()


main()
