from django import forms
from captcha.fields import CaptchaField


# 所哟得表单类
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': ' '}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))  # 指定该字段在form表单里面表现为密码输入框
    captcha = CaptchaField(label="验证码")
