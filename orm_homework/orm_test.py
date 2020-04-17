#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 12:59
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : orm_test.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_homework.settings")
django.setup()
from app01 import models
# 1. 查找所有书名里包含金老板的书
ret = models.Book.objects.filter(title__contains='金老板')
# 2. 查找出版日期是2018年的书
ret = models.Book.objects.filter(publish_date__year=2018)
# 3. 查找出版日期是2017年的书名
ret = models.Book.objects.filter(publish_date__year=2017).values('title')
ret = models.Book.objects.filter(publish_date__year=2017).values_list('title')
# 4. 查找价格大于10元的书
ret = models.Book.objects.filter(price__gt=10)
# 5. 查找价格大于10元的书名和价格
ret = models.Book.objects.filter(price__gt=10).values('title','price')
# 6. 查找memo字段是空的书
from django.db.models import Q
ret = models.Book.objects.filter(Q(memo__isnull=True)|Q(memo=''))
#
# 7. 查找在北京的出版社
ret = models.Publisher.objects.filter(city='北京')
# 8. 查找名字以沙河开头的出版社
ret = models.Publisher.objects.filter(name__startswith='沙河')
# 9. 查找“沙河出版社”出版的所有书籍
ret = models.Book.objects.filter(publisher__name='沙河出版社')#基于字段的查询
# 10. 查找每个出版社出版价格最高的书籍价格
from django.db.models import Max,Min,Count,Avg,Sum
ret = models.Book.objects.values('publisher','publisher__name').annotate(max=Max('price'))
ret = models.Publisher.objects.annotate(max=Max('book__price')).values()
# 11. 查找每个出版社的名字以及出的书籍数量
ret = models.Publisher.objects.annotate(count=Count('book')).values()

# 12. 查找作者名字里面带“小”字的作者
ret = models.Author.objects.filter(name__contains='小')
# 13. 查找年龄大于30岁的作者
ret = models.Author.objects.filter(age__gt=30)

# 14. 查找手机号是155开头的作者
ret = models.Author.objects.filter(phone__startswith='155')


# 15. 查找手机号是155开头的作者的姓名和年龄
ret = models.Author.objects.filter(phone__startswith='155').values('name','age')
# 16. 查找每个作者写的价格最高的书籍价格
ret = models.Author.objects.annotate(max=Max('book__price')).values('name','max')
ret = models.Book.objects.values('author','author__name').annotate(max = Max('price'))
# 17. 查找每个作者的姓名以及出的书籍数量
ret = models.Author.objects.annotate(count= Count('book')).values('name','count')
ret = models.Book.objects.values('author','author__name').annotate(count=Count('id'))
# 18. 查找书名是“跟金老板学开车”的书的出版社
ret= models.Publisher.objects.filter(book__title='跟金老板学开车')#字段查询
book_obj = models.Book.objects.filter(title='跟金老板学开车').first()#对象查询
ret = book_obj.publisher
# 19. 查找书名是“跟金老板学开车”的书的出版社所在的城市  要出版社

ret= models.Publisher.objects.filter(book__title='跟金老板学开车').values('city')#字段查询

# 20. 查找书名是“跟金老板学开车”的书的出版社的名称
ret= models.Publisher.objects.filter(book__title='跟金老板学开车').values('name')#字段查询


# 21. 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
pub_obj = models.Publisher.objects.filter(book__title='跟金老板学开车').first()
ret = pub_obj.book_set.exclude(title='跟金老板学开车').values('title','price')
ret = models.Book.objects.filter(publisher__book__title='跟金老板学开车').exclude(title='跟金老板学开车').values('title','price')
# 22. 查找书名是“跟金老板学开车”的书的所有作者
ret = models.Author.objects.filter(book__title='跟金老板学开车')

book_obj = models.Book.objects.get(title='跟金老板学开车')
ret = book_obj.author.all()
# 23. 查找书名是“跟金老板学开车”的书的作者的年龄
ret = models.Author.objects.filter(book__title='跟金老板学开车').values('name','age')
# 24. 查找书名是“跟金老板学开车”的书的作者的手机号码
ret = models.Author.objects.filter(book__title='跟金老板学开车').values('name','age','phone')
# 25. 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
ret = models.Author.objects.filter(book__title='跟金老板学开车')
# for author in ret:
#     print(author.book_set.values('title','price'))
ret = models.Author.objects.filter(book__title='跟金老板学开车').values('book__title','book__price')
ret = models.Author.objects.values('name','book__title','book__price').filter(book__title='跟金老板学开车')
ret = models.Book.objects.filter(title='跟金老板学开车').values('author__name','author__book__title','author__book__price')
print(ret)

from django.db import transaction

try:
    with transaction.atomic():
        #事务
        #一系列的操作
        pass
except Exception as e:
    print(e)