#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 20:22
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 顺序查找.py
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1