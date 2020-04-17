import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")
import django
django.setup()
from app01 import models
from django.db.models import Avg, Sum, Max, Min, Count,F,Q
from django.db import transaction

try:
    with transaction.atomic():
        #一系列的操作
        models.Book.objects.all().update(repertory=F('repertory') - 10)
        int('sss')
        models.Book.objects.all().update(sale=F('sale') + 10)
except Exception as e:
    print(e)

