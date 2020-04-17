import time

from django.shortcuts import render, redirect, HttpResponse, reverse
from app01 import models
from functools import wraps
from django.utils.decorators import method_decorator
from django.conf import global_settings

def login_required(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        # print(request.COOKIES)
        # is_login = request.COOKIES.get('is_login')
        is_login = request.session.get('is_login')
        print(is_login,type(is_login))
        # if is_login != '1':
        if is_login != 1:
            # 没有登录  跳转到登录页面
            return redirect('/login/?url={}'.format(request.path_info))
        ret = func(request, *args, **kwargs)
        return ret

    return inner


def timer(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        start = time.time()
        ret = func(request, *args, **kwargs)
        print('执行的时间是：{}'.format(time.time() - start))
        return ret

    return inner


# Create your views here.
@login_required
def publisher_list(request):
    # 获取数据库信息
    all_publishers = models.Publisher.objects.all().order_by('id')  # 返回对象列表
    # 返回到页面展示
    # for i in all_publishers:
    #     print(i)
    #     print(i.name)
    #     print(i.id)
    print(request.COOKIES)
    is_login = request.COOKIES.get('is_login')
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})

@login_required
def publisher_add(request):
    # get请求返回一个页面 页面中包含form表单
    """
    判断是不是post请求
    获取数据新增到数据库中
    返回一个重定向到展示出版社的页面
    :param request:
    :return:
    """
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        print(pub_name)
        if not pub_name:
            # 输入为空
            return render(request, 'publisher_add.html', {'error': '不能为空！！'})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html', {'error': '已存在！'})
        ret = models.Publisher.objects.create(name=pub_name)
        print(ret, type(ret))
        return redirect(reverse('publisher'))
    return render(request, 'publisher_add.html')


# 新增出版社 CBV
from django.views import View


# @method_decorator(timer,name='post')
# @method_decorator(timer,name='get')
@method_decorator(login_required, name='dispatch')
class PublisherAdd(View):
    # @method_decorator(timer)
    # def dispatch(self, request, *args, **kwargs):
    #     #之前的操作
    #     ret = super().dispatch(request,*args,*kwargs)
    #     #之后的操作
    #     return ret

    def get(self, request):
        print("get请求被执行")
        # 处理get请求
        return render(request, 'publisher_add.html')

    # @method_decorator(timer)
    def post(self, request):
        print("post请求被执行")
        # 处理post请求
        pub_name = request.POST.get('pub_name')
        # print(pub_name)
        if not pub_name:
            # 输入为空
            return render(request, 'publisher_add.html', {'error': '不能为空！！'})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html', {'error': '已存在！'})
        ret = models.Publisher.objects.create(name=pub_name)
        # print(ret, type(ret))
        return redirect(reverse('publisher'))


def publisher_del(request):
    # 获取删除数据的id
    pk = request.GET.get('pk')  # pk主键
    print(pk)
    # 根据id去数据库进行删除
    # models.Publisher.objects.get(pk=pk).delete()#查询出一个对象然后删除
    models.Publisher.objects.filter(pk=pk).delete()  # 查询出一个对象列表 然后列表中删除
    # 返回重定向到展示出版社的页面
    return redirect(reverse('publisher'))


def publisher_edit(request, pk):
    # pk = request.GET.get('pk')
    pub_obj = models.Publisher.objects.get(pk=pk)
    # get 返回一个页面 页面包含form表单  input有原始数据
    if request.method == 'GET':
        return render(request, 'publisher_edit.html', {'pub_obj': pub_obj})
    else:
        # post
        # 修改数据库中对应的数据
        # 返回重定向到展示出版社的页面
        pub_name = request.POST.get('pub_name')
        pub_obj.name = pub_name  # 只修改了内存地址
        pub_obj.save()  # 修改数据库中这个对象的属性 提交到数据量
        # 返回重定向
        return redirect(reverse('publisher'))

@login_required
def book_list(request):
    # 查询所有的书籍
    all_books = models.Book.objects.all()
    # for book in all_books:
    #     print(book)
    #     print(book.name)
    #     print(book.publisher)#出版社对象
    #     print(book.publisher_id)#出版社id
    #     print(book.publisher,book.publisher.name,book.publisher.pk)
    # 返回 一个页面  页面中包含有书籍数据
    return render(request, 'book_list.html', {'all_books': all_books})

@login_required
def book_add(request):
    error = ''
    if request.method == 'POST':
        book_name = request.POST.get('book_name')  # 获取表单的数据
        pub_id = request.POST.get('pub_id')
        # 判断
        if not book_name:
            # 用户输入为空
            error = '不能为空'
        elif models.Book.objects.filter(name=book_name):
            # 数据库中已经有  名字重复
            error = '名字重复'
        else:
            models.Book.objects.create(name=book_name, publisher_id=pub_id)  # 插入数据
            return redirect('/book_list/')
    # 查询出所有的出版社
    all_publishers = models.Publisher.objects.all()
    return render(request, 'book_add.html', {'all_publishers': all_publishers, 'error': error})

@login_required
def book_del(request):
    # 获取表单数据 id
    pk = request.GET.get('id')
    # 获取要删除的对象
    models.Book.objects.filter(pk=pk).delete()
    # 返回一个页面重定向
    return redirect('/book_list/')

@login_required
def book_edit(request):
    # 查询要编辑对象的id
    pk = request.GET.get('id')
    # 根据id查到要编辑的对象
    book_obj = models.Book.objects.get(pk=pk)
    if request.method == 'POST':
        # post请求
        # 获取要编辑的对象
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        # 编辑对象做对应的修改
        # 方法一
        # book_obj.name = book_name
        # book_obj.publisher_id = pub_id
        # book_obj.publisher_id = pub_id
        # # book_obj.publisher_id = models.Publisher.objects.get(pk=pub_id)
        # book_obj.save()#保存到数据库中
        # 方式二
        models.Book.objects.filter(pk=pk).update(name=book_name, publisher_id=pub_id)
        # 重定向到展示的页面
        return redirect('/book_list/')

    # get请求
    # 返回一个页面  页面包含原始数据
    # 查询出所有的出版社
    all_publishers = models.Publisher.objects.all()

    return render(request, 'book_edit.html', {'book_obj': book_obj, 'all_publishers': all_publishers})

@login_required
def author_list(request):
    # 查询作者
    all_authors = models.Author.objects.all()
    # for author in all_authors:
    #     print(author.name)
    #     print(author.id)
    #     print(author.books,type(author.books))#关系管理对象
    #     print(author.books.all())#所关联的所有对象
    #     print('*' * 30)
    # 返回页面
    return render(request, 'author_list.html', {'all_authors': all_authors})

@login_required
def author_add(request):
    if request.method == 'POST':
        # post
        # 获取表单数据
        author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids')  # 获取多个数据
        # print(author_name,book_ids)
        # 向数据库提交数据
        # 向作者表插入作者信息
        author_obj = models.Author.objects.create(name=author_name)  # 返回一个插入的对象
        # 该作者和提交的书籍绑定多对多的关系
        author_obj.books.set(book_ids)  # 设置多对多的关系
        return redirect('/author_list/')

        # 返回重定向到展示作者页面
    # get
    # 返回一个页面 包含form表单  让用户输入作者姓名  选择作品
    all_books = models.Book.objects.all()
    return render(request, 'author_add.html', {'all_books': all_books})

@login_required
def author_del(request):
    pk = request.GET.get('id')
    models.Author.objects.filter(pk=pk).delete()  # 把书籍的对应关系也删掉  书籍并没有删除
    return redirect('/author_list/')

@login_required
def author_edit(request):
    # 获取要编辑的对象的id
    pk = request.GET.get('id')
    # 根据id获取作者对象
    author_obj = models.Author.objects.get(pk=pk)
    if request.method == 'POST':
        # post
        # 获取表单数据
        author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids')
        # 给对象修改数据
        # 1.修改作者姓名
        author_obj.name = author_name
        author_obj.save()
        # 2.对应关系 作者和书的多对多的关系
        author_obj.books.set(book_ids)  # 重新设置
        # 返回重定向 到展示页面
        return redirect('/author_list/')
    # get

    # 获取所有书籍
    all_books = models.Book.objects.all()
    # 返回一个页面 页面中包含作者姓名 包含代表作
    return render(request, 'author_edit.html', {'author_obj': author_obj, 'all_books': all_books})


import json
from django.http.response import JsonResponse


def get_json(request):
    # 反过来python的字典数据类型变成json格式叫反序列化
    data = {'k1': 'v1'}
    # return HttpResponse(json.dumps({'k1':'v1'}))#dump序列化（字典-》字符串）
    # return JsonResponse(data)#dump序列化（字典-》字符串）
    return JsonResponse(data, safe=False)  # safe=False 可以解析非字典的数据类型【】

@login_required
def delete(request, name, pk):
    print(name, pk)
    # 获取到删除的对象  进行删除
    cls = getattr(models, name.capitalize())  # 反射 第一个参数是类 第二个参数是方法字符串  然后首字母大写
    if not cls:
        return HttpResponse('重新检测表名')
    ret = cls.objects.filter(pk=pk)
    if ret:
        ret.delete()
    else:
        return HttpResponse('要删除的数据不存在！')
    # 返回重定向

    # return redirect(name)  # 重定向可以直接写上urlname  内部有reverse
    return JsonResponse({'status':200,'msg':'del_success'})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        if user == 'lsl' and password == '123':
            # 登录成功后保存登录状态到cookie中
            # url = request.GET.get('url')
            url = request.get_signed_cookie('is_login',salt='s28',default='')
            if url:
                return_url = url
            else:
                return_url = reverse('publisher')
            request.session['is_login'] = 1
            ret = redirect(return_url)
            # ret.set_cookie('is_login', '1')#普通cookie
            # ret.set_signed_cookie('is_login', '1',salt='s28',path='/book_list/')#加密cookie

            return ret
        else:
            error = '用户名或密码错误'

    return render(request, 'login.html', locals())  # locals()函数中的局部变量 返回的是字典


def out(request):
    #清除cookie(某个键值对)
    ret = redirect('/login/')
    # ret.delete_cookie('is_login')
    # del request.session['is_login']
    request.session.pop('is_login')
    #重定向登录页面

    return ret