import hashlib

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from app01 import models
# Create your views here.
from app01.forms import RegForm,ArticleForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        user_obj = models.User.objects.filter(username=username,password=md5.hexdigest(),is_active=True).first()
        if user_obj:
            #登录成功
            #保存登录状态和登录用户名
            request.session['is_login'] = True
            request.session['username'] = user_obj.username
            url = request.GET.get('url')
            if url:
                return redirect(url)
            return redirect('index')
        error = '用户名或密码错误'
    return render(request,'login.html',locals())





def register(request):

    form_ojb = RegForm()
    if request.method == 'POST':
        form_ojb = RegForm(request.POST)
        if form_ojb.is_valid():
            #注册成功
            # print(request.POST)
            # print(form_ojb.cleaned_data)

            # form_ojb.cleaned_data.pop('re_pwd')
            # models.User.objects.create(**form_ojb.cleaned_data)#  **打散
            form_ojb.save()
            return redirect('login')
    return render(request,'regeister.html',{'form_ojb':form_ojb})

def index(request):
    #查询所有文章
    all_article = models.Article.objects.all()
    # is_login = request.session.get('is_login')
    # username = request.session.get('username')
    # print(is_login,username)
    return render(request,'index.html',{'all_article':all_article})


def article(request,pk):
    article_obj = models.Article.objects.get(pk=pk)
    return render(request,'article.html',{'article_obj':article_obj})

def backend(request):

    return render(request, 'dashboard.html')


def logout(request):
    request.session.delete()
    return redirect('index')


def article_list(request):

    all_articles = models.Article.objects.all()
    print(all_articles)
    return render(request,'articles_list.html',{'all_articles':all_articles})


def article_add(request):
    form_obj = ArticleForm()
    if request.method == 'POST':
        form_obj = ArticleForm(request.POST)#拿到form表单
        #开始校验
        if form_obj.is_valid():
            detail = request.POST.get('detail')
            detail_obj = models.ArticleDetail.objects.create(content=detail)

            form_obj.instance.detail_id = detail_obj.pk
            form_obj.save()

            return redirect('article_list')


    return render(request,'article_add.html',{'form_obj':form_obj})


def article_edit(request,pk):
    obj = models.Article.objects.filter(pk=pk).first() #查到一个queryset对象 first拿到第一个 如果没有则返回为null
    form_obj = ArticleForm(instance=obj)
    return render(request,'article_edit.html',{'form_obj':form_obj,'obj':obj})