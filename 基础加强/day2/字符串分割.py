#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 18:44
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : 字符串分割.py
import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

if __name__ == '__main__':
    main()