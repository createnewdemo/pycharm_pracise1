#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 18:43
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 正则替换不良内容.py
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()