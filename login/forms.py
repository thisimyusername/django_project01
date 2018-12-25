from django import forms 
from login import models
from captcha.fields import CaptchaField

class UserForm(forms.Form):
	username = forms.CharField(label="用户名", max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	captcha = CaptchaField(label='验证码')
'''class UserForm(forms.ModelForm):
	class Meta:
		model = models.User
		fields = ['username', 'password']

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, *kwargs)
		self.fields['username'].label = '用户名'
		self.fields['password'].label = '密码'
'''
class RegisterForm(forms.Form):
	username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class':"form-control"}))
	password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label="邮箱", max_length=256, widget=forms.EmailInput(attrs={'class': 'form-control'}))
	