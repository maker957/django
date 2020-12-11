from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


# Create your views here.


def index(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    return render(request, 'blog/index.html')


# 通过login（）视图函数，接受并处理请求
# 每个视图函数都至少接受一个参数，并且是第一位置参数， 该参数封装了当前请求的所有数据；
# request.method中封装了数据请求方法，
# request.POST封装了所有POST请求中的数据，这是一个字典类型
# get('username')中的键‘username’是HTML表单的input元素里‘name’属性定义的值，所以在编写form表单的时候一定不能忘记添加name属性。
def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        message = '请检查填写的内容'
        if login_form.is_valid():  # 数据验证
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'blog/login.html', locals())  # 返回当前所有的本地变量字典

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                print(username, password)
                return redirect('/index')
            else:
                message = '密码不正确！'
                return render(request, 'blog/login.html', locals())
        else:
            render(request, 'blog/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'blog/login.html', locals())


def register(request):
    pass
    return render(request, 'blog/register.html')


def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login")
