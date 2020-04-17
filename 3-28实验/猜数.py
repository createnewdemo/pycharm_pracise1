#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 14:25
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 猜数.py
from random import randint
#编写程序模拟猜数游戏。程序运行时，系统生成一个随机数，然后提示用户进行猜测，并根据用户输入进行必要的提示
#（猜对了、太大了、太小了），如果猜对则提前结束程序，如果次数用完仍没有猜对，提示游戏结束并给出正确答案。
def guessNumber(maxValue,maxTimes):
    #随机生成一个整数
    value=randint(1,maxValue)
    for i in range(maxTimes):
        prompt='请输入您猜的数字:'if i==0 else '请再猜一次:'
        #使用异常处理结构，防止输入不是数字的情况
        try:
            x=int(input(prompt))
        except:
            print('必须输入整形数，且在数字1和',maxValue,'之间')
        else:
            if x==value:
                #猜对了
                print('恭喜您，猜对了!')
                break
            elif x>value:
                print('太大了！')
            else:
                print('太小了！')
    else:
        #次数用完还没猜对，游戏结束，提示正确答案.
        print('游戏结束，您失败了！')
        print('正确答案是：',value)
guessNumber(10,3)

