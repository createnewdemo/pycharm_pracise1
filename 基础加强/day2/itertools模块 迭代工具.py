#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 19:58
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : itertools模块 迭代工具.py
"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
foo = itertools.permutations('ABCD')
print(foo)#<itertools.permutations object at 0x0000022A28C8AF40>
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))