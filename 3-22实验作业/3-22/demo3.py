#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 11:25
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo3.py

num=int(input("请输入任意各位数字不相同的4位数："))
c=num
while c!=6174:
    digits=list(str(c))
    digits.sort(reverse=True)#排列最大数和最小数
    if len(digits)<4:
        digits.append('0')
    a=int(''.join(digits))
    digits.reverse()
    b=int(''.join(digits))
    c=a-b
    print("%d-%d=%d" %(a,b,c))