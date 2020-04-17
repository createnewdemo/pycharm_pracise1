import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")
import django
django.setup()
from app01 import models
from django.db.models import Avg, Sum, Max, Min, Count,F,Q


ret = models.Book.objects.filter(sale__gt=F('repertory')) #where 'sale' > 'repertory'


ret = models.Book.objects.filter(id__lte=3).update(sale=F('sale')*2 + 12)

ret = models.Book.objects.filter(Q(id__lt=3)|Q(id__gt=5)) #或者的关系
ret = models.Book.objects.filter(Q(Q(id__lt=3)|Q(id__gt=5))&Q(name__startswith='lsl')) #与的关系
# ret = models.Book.objects.exclude(id__gte=3,id__lte=5)
"""
Q()

| 或者

& 并且

~ 非

"""

print(ret)