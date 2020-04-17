#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
def main():
    for val in fib(3):
        print(val)


if __name__ == '__main__':
    main()