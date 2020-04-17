#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 11:25
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo4.py

n = int(input("输入有几个人："))
k = int(input("报数停下的位置："))
q = list(range(1, n+1))
c = 1
while len(q) != 1:
    t = []
    for i in q:
        if c != k:
            print("第%d个人报数"%(i))
            t.append(i)
        c += 1
        if c > k:
            c -= k
    q = t
print("最后留下来的是：",q[0])