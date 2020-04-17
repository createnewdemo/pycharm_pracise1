from django.shortcuts import render,HttpResponse

# Create your views here.
def reg(request):
    if request.method == 'POST':
        #获取提交的数据
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        #对数据进行校验
        if len(user) < 6:
            user_error = '用户名不能小于6位'
            return render(request,'reg.html',locals())
        else:

            return HttpResponse('注册成功')

    return render(request,'reg.html')
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def check_name(value):
    #不符合规则
    if 'lsl' in value:
        raise ValidationError("德玛西亚") #捕获错误i
    #符合规则不做任何操作

class RegForm(forms.Form):

    user = forms.CharField(
        label='用户名',
        required=False,
        disabled=False,
        min_length=6,
        validators=[check_name],#校验器
        initial = "张三",
        error_messages={
            "required":"不能为空",
            "invalid":"格式错误",
            "min_length":"用户名最短8位",
        }
                           )
    pwd = forms.CharField(label='密码',widget=forms.PasswordInput)
    re_pwd = forms.CharField(label='确认密码',widget=forms.PasswordInput)
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=(('1','男'),('2','女'),('3','不详'),))
    hobby = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=(('1','吃饭'),('2','睡觉'),('3','买键盘'),))
    phone = forms.CharField(validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式不正确')])
    def clean_user(self):#局部钩子
        #不符合校验规则
        value = self.cleaned_data.get('user')
        if 'lsl' in value:
            raise ValidationError("德玛西亚")  # 捕获错误i
        #符合校验规则
        return value
    def clean(self):#全局钩子
        #不符合校验规则

        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd != re_pwd:
            #将错误信息加入某个字段里面
            self.add_error('re_pwd','两次密码不一致')
            raise ValidationError('两次密码不一致')
        #符合校验规则

        return self.cleaned_data

def reg2(request):
    form_obj = RegForm()
    if request.method == 'POST':
        #对提交的数据做校验
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():#对数据进行校验
            #校验成功
            return HttpResponse('注册成功')
        print(form_obj.cleaned_data)
    return render(request,'reg2.html',{'form_obj':form_obj})