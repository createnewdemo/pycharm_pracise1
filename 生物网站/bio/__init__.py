#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 15:47
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : __init__.py.py
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
s1 = 'hello ' * 3
print(s1) # hello hello hello
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False