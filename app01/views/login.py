from io import BytesIO

from django.shortcuts import render, redirect, HttpResponse
from django import forms
from app01 import models

from app01.utils.auth_code_image import generate_auth_code_image
from app01.utils.encrypt import md5


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})
        )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control','placeholder':'Password'})  
        )
    auth_code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder':'Password',
                                      'autocomplete':'off'})  
        )

    def clean_password(self):
        # 对密码进行MD5加密，并返回加密后的密码
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

def login(request):
    if request.method == "GET":
        form = LoginForm()
        title = "Login"
        return render(request, 'login.html', {'form':form, 'title':title})
    form = LoginForm(data=request.POST)

    # print(request.POST)
    if form.is_valid():
        # 接收用户POST传输过来的信息
        # print("form.cleaned_data", form.cleaned_data)
        # 获取用户填写的验证码，并从字典中删除，以防后面代码的对数据库验证报错(因为数据库中没有auth_code字段)
        user_input_auth_code = form.cleaned_data.pop('auth_code')
        auth_code = request.session.pop('auth_code', '')

        if user_input_auth_code.upper() != auth_code.upper():
            form.add_error("auth_code", "验证码错误")
            return render(request, 'login.html', {'form':form})
    
        # 验证用户提交的登录信息是否存在于数据库中
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        
        # print("验证数据库中是否存在帐号:", admin_object)
            # 存在返回:Admin object (12)
            # 不存在返回None
        # 判断用户信息是否存在
        if not admin_object:
            # 添加错误信息提示,在password的下方显示
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form':form})
    
        # 密码正确时，将用户ID与用户名称写入到session的info 键中
        request.session["info"] = {'id':admin_object.id, 'username':admin_object.username}
        # 设置session超时时间为7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/")
    return render(request, 'login.html', {'form':form})

def logout(request):
    '''注销'''
    request.session.clear()
    return redirect('/login/')

def auth_code(request):
    code, image= generate_auth_code_image(size=(120, 30), position_offset_y=1, point_chance=15, line_num=(1, 3))
    # 将code存入session中，在login视图函数中进行验证
    request.session['auth_code'] = code
    # 设置session 60s超时
    request.session.set_expiry(60)
    stream = BytesIO()
    image.save(stream, 'png')
    return HttpResponse(stream.getvalue())
