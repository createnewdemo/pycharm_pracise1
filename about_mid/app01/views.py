from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def index(request):
    print('index')
    #int('xxx')
    # return HttpResponse('index')
    # return rander(request,'index.html',{'user':'lsl'})
    return TemplateResponse(request,'index.html',{'user':'lsl'})
