#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 20:23
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 合并2个有序列表.py
def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return merge_sort(list(items), comp)