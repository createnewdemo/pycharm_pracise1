#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 11:46
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : csv_demo.py
import csv

header = ['title', 'cid', 'seller_cids']

# data = [
#     ['得力笔记本', '999', '999', '出售', '1', '1', '笔记本', '笔记本', '河南', '信阳', '2020-4-14'],
#     ['张五', '123#456', 'PASS'],
#     ['张#abc123', '123456', 'PASS'],
#     ['666', '123456', 'PASS'],
#     ['a b', '123456', 'PASS']
# ]
data = [
        ['宝贝名称','宝贝类目','店铺类目'],
        ]
# data = {'得力笔记本','得力笔记本','得力笔记本'}

# # 以添加的形式写入csv，跟处理txt文件一样，设定关键字"a"，表追加
# csvFile = open("2.csv", "a")
#
# # 新建对象writer
# writer = csv.writer(csvFile)
#
# # 写入，参数还是列表形式
# writer.writerow(data)
#
# csvFile.close()

with open('3.csv', 'a',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)