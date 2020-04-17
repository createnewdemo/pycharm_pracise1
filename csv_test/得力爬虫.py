#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 12:36
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 得力爬虫.py
import requests
from lxml import etree
import csv
class deli(object):

    def get_goods_url(self):
        url = 'http://www.nbdeli.com/product/product_search.php?keywords=%E8%AE%A2%E4%B9%A6%E6%9C%BA'
        r = requests.get(url).text
        xp = etree.HTML(r)
        res = xp.xpath('//ul[@class="pp-list"]/li')
        self.goods_urls = []
        for p, i in enumerate(res):
            #print("第{}条数据".format(p + 1))
            titles_str = etree.tostring(i, encoding='utf-8').decode('utf-8')
            xp_obj = etree.HTML(titles_str)
            #self.title = xp_obj.xpath('.//div/a/@title')[0]
            goods_url = xp_obj.xpath('.//div/a/@href')[0]
            self.goods_urls.append('http://www.nbdeli.com'+goods_url)
            #print(title,type(title))
            #print(self.goods_urls)
    def get_info(self):
        self.name_list = []
        self.img_url_list = []
        url_list = self.goods_urls
        for p,i in  enumerate(url_list[0:10]):
            print("第{}条数据".format(p + 1))
            #print(i,type(i))
            r = requests.get(i).text
            xp = etree.HTML(r)
            img_url = "http://www.nbdeli.com" + xp.xpath('//div[@class="img-div"]/img/@src')[0]
            self.img_url_list.append(img_url)
            #print(img_url)
            #title = xp.xpath('/html/body/div[4]/div[5]/p[2]/text()')[0]
            del_title = xp.xpath('/html/body/div[4]/div[5]/p[2]/text()')[0]
            self.name_list.append(del_title)
            """下载图片"""
            r = requests.get(img_url)
            print('下载图片%d'%p)
            try:
                with open('F:\pycharm_pracise\csv_test\pen_img\{}.jpg'.format(del_title), 'wb') as f:
                    f.write(r.content)
            except Exception as e:
                print(e)
            """下载详情图片"""
            # detail_img = xp.xpath('//div[@class="p-detail-div"]/p')
            # detail_img_urtl_list = []
            # for i in detail_img[1:-1]:
            #     detail_imgs = i.xpath('./img/@src')
            #     detail_img_urtl_list.append(detail_imgs)
            # try:
            #     Product_specifications = xp.xpath('//div[@class="pd-buy-info"]')[0]
            #     key1 = Product_specifications.xpath('.//p[3]/span[1]/text()')[0]
            #     val1 = Product_specifications.xpath('.//p[3]/span[2]/text()')[0]
            #     key2 = Product_specifications.xpath('.//p[3]/span[3]/text()')[0]
            #     val2 = Product_specifications.xpath('.//p[3]/span[4]/text()')[0]
            #     key3 = Product_specifications.xpath('.//p[3]/span[5]/text()')[0]
            #     val3 = Product_specifications.xpath('.//p[3]/span[6]/text()')[0]
            #     print(key1+':'+val1,key2+':'+val2,key3+':'+val3)
            # except Exception as e:
            #     print(e)
    def writer_info(self):
        header = ['title']
        data = [
            ['宝贝名称']
        ]
        for i in self.name_list:
            del_name_list = [i]
            data.append(del_name_list)
        #print(data)
        with open('pen3.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
spider = deli()
spider.get_goods_url()
spider.get_info()
spider.writer_info()