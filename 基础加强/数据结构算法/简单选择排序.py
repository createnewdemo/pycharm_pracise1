#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 20:05
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 简单选择排序.py
def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

print(select_sort([1,5,6,9,8,4,4,5,8,10,36]))