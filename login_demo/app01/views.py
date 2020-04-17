from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
def login(request):
    # return render(request,'login.html')
    if request.method == 'POST':
        print(request.POST,type(request.POST))
        print(request.POST.get('user'),type(request.POST.get('user')))
        print(request.POST.get('pwd'),type(request.POST.get('pwd')))
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        #进行校验
        # if user == '320783214@qq.com' and pwd == '123':
        if models.User.objects.filter(username=user,password=pwd):
            #校验成功告知登录成功
            return redirect('/index/')#直接写路径
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def index1(request):
    #orm的测试

    ret = models.User.objects.all()# QuerySet 对象列表
    for i in ret:
        print(i,i.username,i.password,type(i.username))


    ret = models.User.objects.get(username='320783214@qq.com',password='123')#获取一条数据
    ret = models.User.objects.filter(password='123')#获取满足条件的对象
    print(ret.username)
    print(ret,type(ret))
    return render(request,'index.html')