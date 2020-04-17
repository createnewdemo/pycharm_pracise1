from django.shortcuts import render,HttpResponse

# Create your views here.
def article(request):
    return HttpResponse('article')



def articles(request):
    return HttpResponse('articles')