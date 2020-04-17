#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 21:21
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 喻峰校园教育厅.py
import json

import requests

cookies = {
    'MOD_AUTH_CAS': 'ST-2020641-AodqiNyAgdV26cZSRhrL1585315980689-CZOn-cas',
    'acw_tc': '76b20ff915853159800047614e054c1ae54d5bcf6840faee768102ad90410a',
    'clientType': 'cpdaily_student',
    'sessionToken': '09d658ed-7521-4677-a0ad-367356c2f529',
    'tenantId': 'hnuahe',
}

headers = {
    'Host': 'hnuahe.cpdaily.com',
    'Content-Type': 'application/json',
    'Cpdaily-Extension': '7Q881vmOiX52ZMMaeIbU2lVKKB2Y2n/yeCgeJmxRk4DDPqL97WnLcwKjBQ1k Gv/6EJKDvK3qW0bQ2JU8b3sNeXGLD4vBn9ZU98qmcvqXRegcBwICAb8mSaFD XOr0I1sUwQzHMUTErHIgm0LZW0VLZmhHyzvjqU63SbteHQOUuGyO4A1kd/aa XHQaH8hl5AzLnlCqq8i6CsUo/0mPrE066I+f0qGsponChgmNDSKzA0M/GA3/ PiBCdNiAm03gdRiPZoTXXLqMZyp3xA49XjO6a3zKeNOfas+A',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
    'User-Agent': '%E4%BB%8A%E6%97%A5%E6%A0%A1%E5%9B%AD/1 CFNetwork/1121.2.2 Darwin/19.3.0',
}
data = {
    "formWid": "259",
    "address": "河南省信阳市商城县",
    "collectWid": "1387",
    "schoolTaskWid": "24964",
    "form": [
        {
            "wid": "1307",
            "formWid": "259",
            "fieldType": 2,
            "title": "你所在的校区",
            "description": "如果你所在的学校只有一个校区，请选择【本校区】；如果有多个校区的，请选择【其他】，并填写校区名称",
            "minLength": 0,
            "sort": "1",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 1,
            "colName": "field001",
            "value": "其他",
            "fieldItems": [
                {
                    "itemWid": "4478",
                    "content": "其他",
                    "isOtherItems": 1,
                    "contendExtend": "英才校区",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1308",
            "formWid": "259",
            "fieldType": 1,
            "title": "你的身份证号",
            "description": "请填入完整18位身份证号",
            "minLength": 18,
            "sort": "2",
            "maxLength": 18,
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field002",
            "value": "411524199801182710",
            "fieldItems": [ ]
        },
        {
            "wid": "1309",
            "formWid": "259",
            "fieldType": 1,
            "title": "你的当前所在地区",
            "description": "请选择你目前所在的省、市、区（县），不在大陆地区的，请选择海外具体地区。",
            "minLength": 1,
            "sort": "3",
            "maxLength": 300,
            "isRequired": 1,
            "imageCount": -2,
            "hasOtherItems": 0,
            "colName": "field003",
            "value": "河南省/信阳市/商城县",
            "fieldItems": [ ],
            "area1": "河南省",
            "area2": "信阳市",
            "area3": "商城县"
        },
        {
            "wid": "1310",
            "formWid": "259",
            "fieldType": 2,
            "title": "你所在的小区（村）是否有确诊情况？",
            "description": "",
            "minLength": 0,
            "sort": "4",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field004",
            "value": "否",
            "fieldItems": [
                {
                    "itemWid": "4480",
                    "content": "否",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1311",
            "formWid": "259",
            "fieldType": 2,
            "title": "共同居住人是否有确诊病例？",
            "description": "",
            "minLength": 0,
            "sort": "5",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field005",
            "value": "否",
            "fieldItems": [
                {
                    "itemWid": "4482",
                    "content": "否",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1312",
            "formWid": "259",
            "fieldType": 2,
            "title": "是否去过湖北疫区？",
            "description": "",
            "minLength": 0,
            "sort": "6",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field006",
            "value": "否",
            "fieldItems": [
                {
                    "itemWid": "4484",
                    "content": "否",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1313",
            "formWid": "259",
            "fieldType": 2,
            "title": "与疫区人员是否有接触？",
            "description": "",
            "minLength": 0,
            "sort": "7",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field007",
            "value": "否",
            "fieldItems": [
                {
                    "itemWid": "4486",
                    "content": "否",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1314",
            "formWid": "259",
            "fieldType": 2,
            "title": "是否留置观察？",
            "description": "",
            "minLength": 0,
            "sort": "8",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field008",
            "value": "否",
            "fieldItems": [
                {
                    "itemWid": "4488",
                    "content": "否",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1315",
            "formWid": "259",
            "fieldType": 2,
            "title": "是否曾经确诊？",
            "description": "",
            "minLength": 0,
            "sort": "9",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field009",
            "value": "否",
            "fieldItems": [
                {
                    "itemWid": "4490",
                    "content": "否",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        },
        {
            "wid": "1316",
            "formWid": "259",
            "fieldType": 2,
            "title": "健康状况是否良好？",
            "description": "",
            "minLength": 0,
            "sort": "10",
            "maxLength": '',
            "isRequired": 1,
            "imageCount": '',
            "hasOtherItems": 0,
            "colName": "field010",
            "value": "是",
            "fieldItems": [
                {
                    "itemWid": "4491",
                    "content": "是",
                    "isOtherItems": 0,
                    "contendExtend": "",
                    "isSelected": 1
                }
            ]
        }
    ]
}
response = requests.post('https://hnuahe.cpdaily.com/wec-counselor-collector-apps/stu/collector/submitForm', headers=headers, cookies=cookies, data=json.dumps(data))


print(response.text)