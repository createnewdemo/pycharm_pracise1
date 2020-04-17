#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 22:29
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : mytags.py
from django import template


register = template.Library()


@register.filter
def add_arg(value,arg):
    #功能
    return "{}_{}".format(value,arg)

@register.simple_tag
def str_join(*args,**kwargs):

    return "{}_{}".format('_'.join(args),'*'.join(kwargs.values()))