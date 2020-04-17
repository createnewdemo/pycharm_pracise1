import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")
import django
django.setup()
from app01 import models
from django.db.models import Avg, Sum, Max, Min, Count
#aggregate  终止子句
# ret = models.Book.objects.all().aggregate(Avg("price"))# 返回字典 #{'price__avg': 205.483333}
# ret = models.Book.objects.all().aggregate(average_price=Avg('price'))# 返回字典{'average_price': 205.483333}
# ret = models.Book.objects.all().aggregate(Avg("price"), Max("price"), Min("price"))# 返回字典{'price__avg': 205.483333, 'price__max': Decimal('999.00'), 'price__min': Decimal('9.90')}
# ret = models.Book.objects.aggregate(Avg("price"), Max("price"), Min("price"))# 返回字典{'price__avg': 205.483333, 'price__max': Decimal('999.00'), 'price__min': Decimal('9.90')}
# ret = models.Book.objects.filter(id__gt=2).aggregate(Avg("price"), Max("price"), Min("price"))# 返回字典{'price__avg': 205.483333, 'price__max': Decimal('999.00'), 'price__min': Decimal('9.90')}
#
# print(ret)

# 分组  group_by

#统计每一本书的作者个数
#annotate注释的意思  添加额外的信息
# ret= models.Book.objects.annotate(Count('authors')).values()
# for i in ret:
#     print(i)

#统计出每个出版社买的最便宜的书的价格
# ret = models.Publisher.objects.annotate(Min('book__price')).values()
#按照pub_id pub_name分组
# ret = models.Book.objects.values('pub','pub__name').annotate(Min('price'))

# publisher_list = models.Publisher.objects.annotate(min_price=Min("book__price"))
# for i in ret:
#     print(i)

#统计不止一个作者的图书
# ret = models.Book.objects.annotate(count=Count('authors')).filter(count__gt=1)
# print(ret)

#根据一本图书作者数量的多少对查询集 QuerySet进行排序
# ret = models.Book.objects.annotate(count=Count('authors')).order_by('-count')
# print(ret)
#查询各个作者出的书的总价格

# ret = models.Author.objects.annotate(sum=Sum('books__price')).values()
# ret = models.Book.objects.values('authors','authors__name').annotate(sum=Sum('price'))
# for i in ret:
#     print(i)