from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)#对应数据库varchar(32)
    password = models.CharField(max_length=32)
