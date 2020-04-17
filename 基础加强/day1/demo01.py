#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
def foo():
    pass
def bar():
    pass
"""
输出99乘法表  注意\t的使用

"""
def chengfa():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')#\t	横向制表符
        print()
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()