# -*- coding: gbk -*-
import requests


def COV():
    url = 'https://api.yonyoucloud.com/apis/dst/ncov/country'
    Headers = {
        'apicode': '1aaef2983911441ba03470a297b1c163'
    }
    r = requests.get(url, headers=Headers).json()
    currentConfirmedCount = r['data']['currentConfirmedCount']  # 现存确诊（去掉已经治愈）
    currentConfirmedAdd = r['data']['currentConfirmedAdd']  # 较昨日增加或减少
    suspectedCount = r['data']['suspectedCount']  # 现存疑似
    suspectedAdd = r['data']['suspectedAdd']  # 疑似增加
    curedCount = r['data']['curedCount']  # 累计治愈
    updateTime = r['data']['updateTime']  # 更新时间
    # print(updateTime)
    info = [currentConfirmedCount, currentConfirmedAdd, suspectedCount, suspectedAdd, curedCount, updateTime,
            updateTime]
    text = '现存确诊（去掉已经治愈）:' + str(info[0]) + '\n较昨日增加或减少:' + str(info[0]) + '\n现存疑似:' + str(info[0]) + '\n疑似增加:' + str(
        info[0]) + '\n累计治愈:' + str(info[0]) + '\n更新时间:' + str(info[0])
    print(text)


COV()

# if msg_content == '新冠数据':
#     try:
#         time.sleep(1)
#         eng = self.get_news()[0]
#         info = self.COV()
#         text = """
#         现存确诊（去掉已经治愈）+info['currentConfirmedCount']\n
#         较昨日增加或减少+info['currentConfirmedAdd']\n
#         现存疑似 + info['suspectedCount']\n
#         疑似增加 + info['suspectedAdd']\n
#         累计治愈 + info['curedCount']\n
#         更新时间 + info['updateTime']
#         """
#
#         self.wx.send_text(to_user=self.wx_id, msg=text)
#
#     except Exception as error:
#         print(error)
