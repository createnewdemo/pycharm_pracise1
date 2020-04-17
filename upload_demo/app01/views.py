from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
class Upload(View):
    def get(self,request):
        return render(request,'upload.html')
    def post(self,request):
        print(request.POST)
        print(request.FILES)
        file = request.FILES.get('f1')
        with open(file.name,'wb') as f:
            for i in file:
                f.write(i)
        print(file)
        return HttpResponse('ok')

