#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):#如果是5到1倒着取，则应写为range(5,0,-1)就像是数学中的区间---前闭后开
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    """求最小公倍数"""
    """
    “/”，这是传统的除法，3/2=1.5
    “//”，在python中，这个叫“地板除”，3//2=1
    “%”，这个是取模操作，也就是区余数，4%2=0，5%2=1
    """
    return x * y // gcd(x, y)
if __name__ == '__main__':
    print(lcm(5,10))