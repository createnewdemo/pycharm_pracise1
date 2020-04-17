#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 20:02
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : collections模块.py
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
"""
`Counter`：`dict`的子类，键是元素，值是元素的计数，
它的`most_common()`方法可以帮助我们获取出现频率最高的元素。返回一个列表 元素为元组
[('eyes', 8), ('the', 5), ('look', 4)]
"""
counter = Counter(words)
print(counter.most_common(3))