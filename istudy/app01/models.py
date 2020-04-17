from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class User(models.Model):
    """
    员工信息用户表 密码  职位 公司名（子，总公司）  手机 最后一次登录时间
    """

    username = models.CharField(max_length=32,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=32,verbose_name='密码')
    position = models.CharField(max_length=32,verbose_name='职位')
    company = models.CharField(verbose_name='公司',choices=(('1', '黄土高坡总公司'), ('2', '家里蹲分公司'), ('3', '德玛西亚分公司')),max_length=32)
    phone = models.CharField(max_length=32,verbose_name='手机号')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    last_time = models.DateTimeField(null=True, blank=True,verbose_name='上次登陆时间')
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='img/avatar', default='img/avatar/default.jpg')
    def __str__(self):
        return self.username
    # class Meta:
    #     db_table= ''

class Category(models.Model):

    title = models.CharField(max_length=32,verbose_name='板块标题')
    def __str__(self):
        return self.title

class Article(models.Model):
    """
    标题，文章内容 作者  板块 创建时间  更新时间  删除状态

    """
    title = models.CharField(max_length=64,verbose_name='文章标题')
    abstract = models.CharField(max_length=256,verbose_name='文章摘要')
    # content = models.TextField(verbose_name='文章内容',blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,verbose_name='作者')
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,blank=True,null=True,verbose_name='分类')
    creat_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    publish_status = models.BooleanField(choices=((False,'未发布'),(True,'发布')),default=False,verbose_name='发布状态')
    detail = models.OneToOneField('ArticleDetail',on_delete=models.DO_NOTHING)
    def show_publish_status(self):
        color_dict = {True:'green',False:'#772a4d'}
        return mark_safe('<span style="background: {};color: white;padding: 3px">{}</span>'.format(color_dict[self.publish_status],self.get_publish_status_display()))

class ArticleDetail(models.Model):
    """
    文章详情
    """
    content = models.TextField(verbose_name='文章内容')

class Comment(models.Model):
    """
    评论表
        评论者  评论内容  评论文章  时间 审核状态
    """
    author = models.ForeignKey(verbose_name='评论者',to=User,on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name='评论内容')
    article = models.ForeignKey(verbose_name='文章',to=Article,on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(verbose_name='审核状态',default=True)
