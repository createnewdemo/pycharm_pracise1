#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
# 创建字典的字面量语法
scores = {'李世林': 95, '白元芳': 78, '狄仁杰': 82}
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')#语法糖
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))

# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)