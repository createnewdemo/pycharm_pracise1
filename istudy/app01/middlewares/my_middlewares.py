#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:17
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : my_middlewares.py
from django.shortcuts import redirect, reverse
from django.utils.deprecation import MiddlewareMixin

from app01 import models
from istudy import settings
from django.conf import global_settings, settings
import re


class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 需要登陆后访问的地址需要判断登录状态
        # 默认所有的的地址都要登录才能访问
        # 设置一个白名单 不登录就能访问
        url = request.path_info
        # 校验登录状态

        is_login = request.session.get('is_login')
        if is_login:
            # 已经登录了
            obj = models.User.objects.filter(pk=request.session['pk']).first()
            # print(obj.avatar)
            # print(obj.avatar.url)  # 拼接的路径时settings中设置的 MEDIA_URL = '/media/'
            request.user_obj = obj  # 赋值一个用户对象  以后用不用在通过数据库查询  千万不用命名request.user
            return

        # 白名单

        for i in settings.WHILE_LIST:
            if re.match(i, url):
                return

        # 没有登录  需要i去登录
        return redirect("{}?url={}".format(reverse('login'), url))
