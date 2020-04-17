import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

import django

django.setup()
from app01 import models
ret = models.Person.objects.filter(pid__lt=5)  #less  than 小于
ret = models.Person.objects.filter(pid__gt=5)  #greater  than 大于
ret = models.Person.objects.filter(pid__lte=5)  #less  than equal 小于等于


ret = models.Person.objects.filter(pid__range=[1,6])  #左右都包含 范围
ret = models.Person.objects.filter(pid__in=[1,5,6])  #左右都包含  成员判断

ret = models.Person.objects.filter(name__contains='lsl')  # like 模糊查询
ret = models.Person.objects.filter(name__icontains='lsl')  # like 模糊查询 忽略大小写
ret = models.Person.objects.filter(name__startswith='l')  # like 模糊查询 以什么开头
ret = models.Person.objects.filter(name__istartswith='l')  # like 模糊查询 以什么开头 忽略大小写
# ret = models.Person.objects.filter(name__endwith='l')  # like 模糊查询 以什么结尾
# ret = models.Person.objects.filter(name__iendwith='l')  # like 模糊查询 以什么结尾 忽略大小写

ret = models.Person.objects.filter(birth__year='2020')  # like 模糊查询 以什么结尾 忽略大小写
ret = models.Person.objects.filter(birth__month='1')  # like 模糊查询 以什么结尾 忽略大小写
ret = models.Person.objects.filter(birth__day='1')  # like 模糊查询 以什么结尾 忽略大小写
ret = models.Person.objects.filter(birth__contains='-02-')  # like 模糊查询 以什么结尾 忽略大小写

ret = models.Person.objects.filter(name__isnull=True) #字段为空


print(ret)