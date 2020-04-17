#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 10:01
def Get_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input('请输入一个大于 2 的自然数：'))
s = list()
for i in range(2, n):
    if Get_num(i) == True:
        s.append(i)
print('小于该数字的所有素数组成的列表为：', s)