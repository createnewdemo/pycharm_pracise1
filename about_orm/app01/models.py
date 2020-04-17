from django.db import models

# Create your models here.
class Person(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(db_column='nick',max_length=32,blank=True,null=True) #char
    age = models.IntegerField()
    birth = models.DateTimeField(auto_now=True)# 新增数据是自动保存
    #auto_now_add=True 新增数据时自动保存当前的时间
    #auto_now=True 新增和编辑 数据时自动保存当前的时间

    class Meta:
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "Person"

        # admin中显示的表名称
        verbose_name = '个人信息'

        # verbose_name加s
        verbose_name_plural = '所有用户信息'

        # # 联合索引
        # index_together = [
        #     ("name", "age"),  # 应为两个存在的字段
        # ]
        #
        # # 联合唯一索引
        # unique_together = (("name", "age"),)  # 应为两个存在的字段
    def __str__(self):

        return "{}-{}".format(self.name,self.age)







class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社名称')
    def __str__(self):
        return "<Publisher object:{}-{}>".format(self.pk,self.name)



class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书名')
    pub = models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name='books',related_query_name='book')
    price = models.DecimalField(max_digits=5,decimal_places=2) #999.99
    sale = models.IntegerField()
    repertory = models.IntegerField()#库存
    def __str__(self):
        return "<Book object:{}-{}>".format(self.pk,self.name)


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='姓名')
    books = models.ManyToManyField('Book',related_name='authors')
    def __str__(self):
        return "<Author object:{}-{}>".format(self.pk,self.name)
