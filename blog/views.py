from django.shortcuts import render
from django.shortcuts import redirect
from . import models


# Create your views here.


def index(request):
    pass
    return render(request, 'blog/index.html')


# 通过login（）视图函数，接受并处理请求
# 每个视图函数都至少接受一个参数，并且是第一位置参数， 该参数封装了当前请求的所有数据；
# request.method中封装了数据请求方法，
# request.POST封装了所有POST请求中的数据，这是一个字典类型
# get('username')中的键‘username’是HTML表单的input元素里‘name’属性定义的值，所以在编写form表单的时候一定不能忘记添加name属性。
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容'

        if username.strip() and password:  # strip()减除无效空格
            try:  # 防止数据库查询失败的异常。
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'blog/login.html', {'message': message})
            if user.password == password:
                print(username, password)
                return redirect('/index')
            else:
                message = '密码不正确！'
                return render(request, 'blog/login.html', {'message': message})
        else:
            return render(request, 'blog/login.html', {'message': message})
    return render(request, 'blog/login.html')


def register(request):
    pass
    return render(request, 'blog/register.html')


def logout(request):
    pass
    return redirect("/login")
