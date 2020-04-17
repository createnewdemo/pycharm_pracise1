from django.shortcuts import render,HttpResponse,reverse

# Create your views here.
def blog(request):
    url = reverse('blog')  #-->>app01/blog
    print(url)


    return HttpResponse('blog')


def blogs(request,year):
    print(year,type(year))
    return HttpResponse('blogs')


def index(request):
    return render(request,'index.html')