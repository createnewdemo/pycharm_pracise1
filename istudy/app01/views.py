import hashlib

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from app01 import models
# Create your views here.
from app01.forms import RegForm, ArticleForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        user_obj = models.User.objects.filter(username=username, password=md5.hexdigest(), is_active=True).first()
        if user_obj:
            # 登录成功
            # 保存登录状态和登录用户名
            request.session['is_login'] = True
            request.session['username'] = user_obj.username
            request.session['pk'] = user_obj.pk
            url = request.GET.get('url')
            if url:
                return redirect(url)
            return redirect('index')
        error = '用户名或密码错误'
    return render(request, 'login.html', locals())


def register(request):
    form_ojb = RegForm()
    if request.method == 'POST':
        form_ojb = RegForm(request.POST, request.FILES)
        if form_ojb.is_valid():
            # 注册成功
            # print(request.POST)
            # print(form_ojb.cleaned_data)

            # form_ojb.cleaned_data.pop('re_pwd')
            # models.User.objects.create(**form_ojb.cleaned_data)#  **打散
            form_ojb.save()
            return redirect('login')
    return render(request, 'regeister.html', {'form_ojb': form_ojb})


def index(request):
    # 查询所有文章
    all_article = models.Article.objects.all()
    # is_login = request.session.get('is_login')
    # username = request.session.get('username')
    # print(is_login,username)
    # obj = models.User.objects.filter(pk=request.session['pk']).first()
    # print(obj.avatar)
    # print(obj.avatar.url) #拼接的路径时settings中设置的 MEDIA_URL = '/media/'
    return render(request, 'index.html', {'all_article': all_article})


def article(request, pk):
    article_obj = models.Article.objects.get(pk=pk)
    return render(request, 'article.html', {'article_obj': article_obj})


def backend(request):
    return render(request, 'dashboard.html')


def logout(request):
    request.session.delete()
    return redirect('index')


def article_list(request):
    all_articles = models.Article.objects.filter(author=request.user_obj)
    print(all_articles)
    return render(request, 'articles_list.html', {'all_articles': all_articles})


def article_add(request):
    obj = models.Article(author=request.user_obj)
    form_obj = ArticleForm(instance=obj)  # 什么都不传
    if request.method == 'POST':
        form_obj = ArticleForm(request.POST, instance=obj)  # 拿到form表单
        # 开始校验
        if form_obj.is_valid():
            # 获取文章详情字符串
            detail = request.POST.get('detail')
            # 创建文章详情对象
            detail_obj = models.ArticleDetail.objects.create(content=detail)
            form_obj.instance.detail_id = detail_obj.pk
            form_obj.save()  # form_obj.instance.save（）
            return redirect('article_list')
    return render(request, 'article_add.html', {'form_obj': form_obj})


# 关联了俩个表
def article_edit(request, pk):
    obj = models.Article.objects.filter(pk=pk).first()  # 查到一个queryset对象 first拿到第一个 如果没有则返回为null
    form_obj = ArticleForm(instance=obj)  # 传了个instance对象
    if request.method == 'POST':
        form_obj = ArticleForm(request.POST, instance=obj)  # 包含数据库没修改之前的数据  以及表单提交的数据
        if form_obj.is_valid():  # 通过校验
            form_obj.instance.detail.content = request.POST.get('detail')
            form_obj.instance.detail.save()  # 修改以后 还要保存 文章详情
            form_obj.save()  # 保存文章的信息
    return render(request, 'article_edit.html', {'form_obj': form_obj, 'obj': obj})
