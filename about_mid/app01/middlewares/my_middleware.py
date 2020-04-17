#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 15:56
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : my_middleware.py
from django.shortcuts import render,HttpResponse
from django.utils.deprecation import MiddlewareMixin
import time
class MD1(MiddlewareMixin):
    def process_request(self,request):

        print('MD1')
        #return HttpResponse('md1')

    def process_response(self,request,response):
        print('md1 process_response')
        return response
    def process_view(self,request,view_func,view_args,view_kwargs):

        print('md1 process_view')
    def process_exception(self,request,exception):
        print('md1 process_exception')
        return HttpResponse('异常处理好啦')
    def process_template_response(self,request,response):
        print('md1 process_template_response')
        return response
class MD2(MiddlewareMixin):
    def process_request(self,request):
        print('MD2')
        #return HttpResponse('md2 ')
    def process_response(self,request,response):
        print('md2 process_response')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('md2 process_view')


visit_history = {
    # ip : [19:55:05,19:55:06,19:55:07]
}

class Throttle(MiddlewareMixin):

    def process_request(self,request):

        print('Throttle')
        print(request.path_info)
        ip = request.META.get('REMOTE_ADDR')

        history = visit_history.get(ip,[]) #如果第一次拿是空的列表 就把当前ip赋值到空的列表中
        #第一次history  []
        #第二次history [19:55:05]
        #第三次 history[19:55:05,19:55:06]
        #第四次 history[19:55:05,19:55:06，19:55:07]


        now = time.time()
        new_history = []
        for i in history:#
            if now - i < 5:
                new_history.append(i)
        visit_history[ip] = new_history
        if len(new_history) >= 3:
            return HttpResponse('你的手速太快了，歇一会')

        new_history.append(now)



class Throttle(MiddlewareMixin):

    def process_request(self,request):

        ip = request.META.get('REMOTE_ADDR')
        history = visit_history.get(ip,[]) #如果第一次拿是空的列表 就把当前ip赋值到空的列表中



        now = time.time()

        while history and now - history[-1] > 5:
            history.pop()

        if len(history) >= 3:
            return HttpResponse('你的手速太快了，歇一会')

        history.insert(0,now)#在第一个位置插入
