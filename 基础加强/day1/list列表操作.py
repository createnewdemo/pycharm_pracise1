#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
# 通过循环用下标遍历列表元素
list1 = [1, 3, 5, 7, 100]
for index in range(len(list1)):
    print(list1[index])

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):#index为索引的下标
    print(index, elem)
list2 = [1,3,5]
# 添加元素
list1.append(200)
list1.insert(1, 400)
list1.append(list2)
"""
Extend是把每个元素都作为一个独立的元素扩充到原来的列表，
而append则是把整个扩充列表作为一个元素追加到列表最后。
list1 = [1,2,4]
list2 =[[12,6],123]
list1.append(list2)
>>>[1, 2, 4, [[12,6], 123]]
list1.extend(list2)
>>>[1, 2, 4, [12, 6],123]
"""

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)