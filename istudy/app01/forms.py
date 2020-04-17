#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:09
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : forms.py
from django import forms
import hashlib

from django.core.exceptions import ValidationError

from app01 import models


class RegForm(forms.ModelForm):

    # username = forms.CharField()
    password = forms.CharField(error_messages={'required':'这是必填项'},widget=forms.PasswordInput(attrs={'placeholder':'密码','type':'password'}),label='密码',min_length=6)
    re_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'确认密码','type':'password'}),label='确认密码',min_length=6)
    class Meta:
        model = models.User
        # fields = ['username','password']
        fields = '__all__'
        exclude = ['last_time']
        # labels = {
        #     'username':'用户名'
        # }
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'用户名'}),
            'position':forms.TextInput(attrs={'placeholder':'请输入职位'}),
            # 'company':forms.Select(),
            'phone':forms.TextInput(attrs={'placeholder':'手机号'}),
        }
        error_messages = {
            'username':{
                'required':'必填项'

            },
            'password':{
                'required':'必填项'
            }
        }

    #局部钩子
    def clean_phone(self):
        import re
        phone = self.cleaned_data.get('phone')
        if re.match(r'^1[3-9]\d{9}$',phone):
            return phone
        raise ValidationError('手机号格式不正确')
    #全局钩子
    def clean(self):
        self._validate_unique = True  #数据库校验唯一
        password = self.cleaned_data.get('password','')
        re_pwd = self.cleaned_data.get('re_pwd')

        if password == re_pwd:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            print(md5.hexdigest())
            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        self.add_error('re_pwd','两次密码输入不一致')
        raise ValidationError('两次输入不一致')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #自定义操作
        field = self.fields['company']
        choices = field.choices
        choices[0] = ('','选择公司')
        field.choices = choices


class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article  # 只能是model
        fields = "__all__"
        exclude = ['detail']
        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-control'})
        # }

    # def __init__(self,request,*args,**kwargs):
    #     # 获取到用户床来的其他参数request 不要往下面的__init__方法中传了
    #
    #     super().__init__(*args,**kwargs)#执行父类方法
    #     #自定义的操作
    #     # self.fields 是个有序字典 字典中的值就是字段的对象
    #     for field in self.fields.values():#field 就是models中定义的字段
    #         field.widget.attrs['class'] = 'form-control'#field.widgrt
    #         # 是拿到对应的插件的对象field.widget.attrs 然后拿到对应的属性做修改
    #     #修改choice参数
    #     self.fields['author'].choices = [(request.user_obj.pk,request.user_obj.username)]
    def __init__(self, *args, **kwargs):
        # 获取到用户床来的其他参数request 不要往下面的__init__方法中传了

        super().__init__(*args, **kwargs)  # 执行父类方法
        # 自定义的操作
        # self.fields 是个有序字典 字典中的值就是字段的对象
        for field in self.fields.values():  # field 就是models中定义的字段
            field.widget.attrs['class'] = 'form-control'  # field.widgrt
            # 是拿到对应的插件的对象field.widget.attrs 然后拿到对应的属性做修改
        # 修改choice参数

        self.fields['author'].choices = [(self.instance.author_id, self.instance.author.username)]

    # def clean(self):#全局钩子
    #     # form_obj.save()#保存  要插入两张表的内容不用这个
    #     # 插入文章详情
    #     detail = self.data.get('detail')
    #     # print(detail)
    #     detail_obj = models.ArticleDetail.objects.create(content=detail)  # 拿到文章详情对象
    #     # 往文章里插入内容
    #     # form_obj.cleaned_data  星星打散就可以拿到生成的表单中数据  但是还有自己创建的没加上
    #     # 额外加一个
    #     # 插入文章
    #     self.cleaned_data['detail_id'] = detail_obj.pk
    #
    #     return self.cleaned_data
