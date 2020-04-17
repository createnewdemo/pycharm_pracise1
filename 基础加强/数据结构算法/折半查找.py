#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 20:22
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 折半查找.py
def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1