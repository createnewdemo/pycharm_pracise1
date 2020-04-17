from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        i3 = int(i1)  +  int(i2)

    return render(request,'index.html',locals())


def calc(request):
    x1=request.GET.get('x1')
    x2=request.GET.get('x2')
    x3 = int(x1) + int(x2)
    print(x3)
    return HttpResponse(x3)

import json

from django.http.response import JsonResponse

def test(request):
    print(request.GET)
    hobby = json.loads(request.GET.get('hobby'))#反序列化

    print(hobby,type(hobby))
    return JsonResponse({'status':200,'msg':'ok','error':''})

from django.views.decorators.csrf import csrf_exempt,csrf_protect,ensure_csrf_cookie

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        f1 = request.FILES.get('f1')
        with open(f1.name,'wb') as f:
            for i in f1:
                f.write(i)
        return HttpResponse('ok')
    return render(request,'upload.html')
