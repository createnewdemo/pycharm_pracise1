#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 13:24
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 闭包.py
def outer():
    name = 'lsl'
    def inner():
        print("在inner里打印外层函数的变量",name)
    return inner #注意这里只是返回inner的内存地址 并未执行
print(outer())#<function outer.<locals>.inner at 0x0000019889EAC670>
f = outer() #<function outer.<locals>.inner at 0x0000019889EAC670>
f()#相当于执行的是inner 在inner里打印外层函数的变量 lsl
#此时outer已经执行完毕 正常情况下outer里的内存都被释放了  但是此时因为有闭包的存在 我们却还可以调用inner
#并且inner内部还调用了上一层outer里的name变量  这种粘粘糊糊的现象就是闭包

"""
闭包的意义 ：返回的函数对象 不仅仅是一个函数对象 在该函数外还包裹了一层作用域  这使得 该函数无论在何处调用 优先
使用自己外层包裹的作用域
"""