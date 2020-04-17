import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

import django

django.setup()
from app01 import models
author_obj = models.Author.objects.get(pk=1)

print(author_obj.books)  #关系管理对象
print(author_obj.books.all())  #所关系对象集合

book_obj = models.Book.objects.get(pk=2)
# print(book_obj.author_set.all())
print(book_obj.authors.all())



# ret = models.Book.objects.filter(authors__name='李世林')
# ret = models.Author.objects.filter(books__name='书2')


#关系管理对象的方法
#all  查询所有的对象
#set  设置多对多 的关系 [id,id]
# author_obj.books.set([1,2])
#
# author_obj.books.set(models.Book.objects.filter(id__in=[3,4]))

#add  添加多对多关系
# author_obj.books.add(1,2)
# author_obj.books.add(*models.Book.objects.filter(id__in=[5,6]))#列表打散  变成对象

#remove  添加多对多的关系
# author_obj.books.remove(3,4)
# author_obj.books.remove(*models.Book.objects.filter(id__in=[5,6]))

#clear 清空多对多的关系
# author_obj.books.clear()

# create  新建一个对象和当前的对象建立关系
# author_obj.books.create(name='sdawd',pub_id='1')
ret= book_obj.authors.create(name='adadadfdcvxdc')
print(ret)