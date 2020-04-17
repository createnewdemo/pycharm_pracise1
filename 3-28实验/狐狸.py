#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 14:29
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 狐狸.py

from random import choice, randrange


def catchMe(n=5, maxStep=3):
    '''
    抓狐狸游戏
    :param n: 洞口的个数，默认为5
    :param maxStep: 最大抓取次数，默认允许抓10次
    :return: null
    '''
    # 共有n个洞口，设有狐狸的为1，没有的为0
    positions = [0] * n
    # 狐狸的随机初始位置
    oldPos = randrange(0, n)
    positions[oldPos] = 1

    # 抓maxStep次
    while maxStep >= 0:
        maxStep -= 1
        # 这个循环是为了保证用户输入是否是有效的洞口
        while True:
            try:
                x = input("今天打算打开哪个洞口？（0-{0}）:".format(n - 1))
                # 如果输入的不是数字，会跳转到except部分
                x = int(x)
                # 如果输入的洞口有效，结束这个循环，否则继续输入
                assert 0 <= x < n, "要按套路来啊，再给你一次机会哈！"
                break
            except:
                # 如果输入的不是数字，就执行这里的代码
                print("你要按套路来啊！再给你一次机会！")
        if positions[x] == 1:
            print("成功！我抓到狐狸了！")
            break
        else:
            print("今天没有抓到狐狸。")

        # 如果这次没抓到，则狐狸就会跳到隔壁的洞口
        # 分三种情况：如果在最左边，则只能往右边洞口跳
        # 如果在最右边，则只能往左边洞口跳
        # 如果在中间三个洞头则随机向左右两边洞口跳
        if oldPos == n - 1:  # 在最右边
            newPos = oldPos - 1
        elif oldPos == 0:  # 在最左边
            newPos = oldPos + 1
        else:
            newPos = oldPos + choice((-1, 1))
        positions[oldPos], positions[newPos] = 0, 1
        oldPos = newPos
    else:
        print("十天了！放弃吧！！")


# 启动游戏
catchMe()