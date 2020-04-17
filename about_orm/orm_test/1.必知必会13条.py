import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

import django

django.setup()
from app01 import models

# all 查询所有的数据  QuerySet  对象列表  【对象，对象 】
ret = models.Person.objects.all()

# get  获取一个有且唯一的数据  对象   没有或者多个就报错
ret = models.Person.objects.get(pk=1)

# filter  获取满足条件的数据  对象列表  【对象，对象 】
ret = models.Person.objects.filter(pk=1)

# exclude  获取不满足条件的数据  对象列表  【对象，对象 】
ret = models.Person.objects.exclude(pk=1)

# order_by 排序 默认升序  字段前加- 降序排序 多字段排序
ret = models.Person.objects.all().order_by('-age','-pid')

# reverse  对已经排序的对象列表进行翻转
ret = models.Person.objects.all().order_by('pid').reverse()

# values 不指定字段 获取数据所有的字段名和值  QuerySet   [ {},{} ]
# 指定字段 获取数据指定的字段名和值  QuerySet
ret = models.Person.objects.all().values('pid','name')


# values_list 不指定字段 获取数据所有的值  QuerySet   [ (),() ]
# 指定字段 获取数据指定字段的值  QuerySet
ret = models.Person.objects.all().values_list('name','pid')

#  distinct 去重
ret = models.Person.objects.values('age').distinct()

# count 计数
ret = models.Person.objects.all().count()

# first 获取第一个元素
ret = models.Person.objects.all().first()

# last 获取最后一个元素
ret = models.Person.objects.all().last()

# exists  判断是否有结果
ret = models.Person.objects.filter(pk=10).exists()


print(ret)

"""
返回对象列表 
all 
filter  
exclude
order_by 
reverse
values  [{},{}]
values_list     [(),() ]
distinct 

返回对象 
get  
first 
last 

返回数字
count

返回布尔值
exists


"""
