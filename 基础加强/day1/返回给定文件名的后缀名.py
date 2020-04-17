#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:48
# @Author  : lihanhan
# @Email   : demo1li@163.com
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
