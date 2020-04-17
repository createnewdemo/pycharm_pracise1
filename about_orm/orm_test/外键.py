import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

import django

django.setup()
from app01 import models

#基于对象的查询
#正向查询
book_obj = models.Book.objects.get(pk=1)
# print(book_obj.pub)  #关联的出版社对象
# print(book_obj.pub_id)  #关联的出版社id

#反向查询
pub_obj = models.Publisher.objects.get(pk=1)
print(pub_obj)
# print(pub_obj.book_set,type(pub_obj.book_set))  #类名小写 set  关联所有对象
# print(pub_obj.book_set.all())
#指定related_name=‘books’
# print(pub_obj.books,type(pub_obj.books))  #类名小写 set  关联所有对象
# print(pub_obj.books.all())

#基于字段查询
ret = models.Book.objects.filter(pub__name__contains='出版社1')


# #不指定related_name='books'
# ret = models.Publisher.objects.filter(book__name='书1')

# #指定related__name='books' 不指定related_query_name='book'
# ret = models.Publisher.objects.filter(books__name='书1')

#指定related_query_name='book'
# ret = models.Publisher.objects.filter(book__name='书1')
# print(ret)


#  set add  create  只有对象  没有id
pub_obj.books.set(models.Book.objects.filter(id__in=[1,2]))

# remove  clear 不能用