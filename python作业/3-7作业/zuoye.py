#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 11:57
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : zuoye.py

# num1 = input("请输入第一个数:")
# num2 = input("请输入第二个数:")
# sum = int(num1[0]) + int(num2[0])
#
# setA={1,2,3,4}
# setB={3,4,5,6}
# print(setA&setB)#交集
# print(setA-setB)#差集
# print(setA|setB)#并集

# a = int(input("请输入一个十进制整数："))
# print("{}对应二进制为{:b},八进制为{:o},"
#       "十六进制为{:x}".format(a,a,a,a))
# x = int(input("请输入一个自然数："))
# print("转换为2进制为：{}".format(bin(x)))
# print("转换为8进制为：{}".format(oct(x)))
# print("转换为216进制为：{}".format(hex(x)))


# lstA = eval(input("请输入一个列表如：[1,2]:"))
#
# lstB =sorted(lstA,reverse=True)
#
# print("排序列表为:",lstB)


#
a = eval(input("首项:"))
q = eval(input("公比:"))
n = eval(input("项数:"))
A = []
j = 0
for i in range(n):#a×q^(n-1) 通项公式
    k = a * (q ** i)#**幂 - 返回x的y次幂
    A.append(k)
for m in A:
    j = j + int(m)
print("结果:",j)



