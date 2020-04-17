#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False#注意这种判断语句的写法！
def is_palindrome(num):
    """ 判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0 :#temp等于0时退出循环
        total = total * 10 + temp % 10#total第一次取出个位数字 第二次取最后2位数字
        temp //= 10#取出除了total的其他数字
    return total == num #把目标的数字反转完毕退出循环 最后和赋值的num比较
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('输入有误！')