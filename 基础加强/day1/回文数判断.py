#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
#121 正读反读都一样
def is_palindrome(num):
    """ 判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0 :#temp等于0时退出循环
        total = total * 10 + temp % 10#total第一次取出个位数字 第二次取最后2位数字
        temp //= 10#取出除了total的其他数字
    return total == num #把目标的数字反转完毕退出循环 最后和赋值的num比较
if __name__ == '__main__':
    print(is_palindrome(525))

