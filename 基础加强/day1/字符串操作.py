#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
# 检查字符串是否以数字和字母构成  !!
print(str2.isalnum())

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
'''
Python 3.6以后，格式化字符串还有更为简洁的书写方式
就是在字符串前加上字母`f`，
我们可以使用下面的语法糖来简化上面的代码。
'''
print(f'{a} * {b} = {a * b}')