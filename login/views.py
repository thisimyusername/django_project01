# login/views.py
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from login import models
from login import forms 
import hashlib
import datetime


def index(request):
    pass
    return render(request, 'login/index.html')

# 错误1   have no attibute "cleaned——data" 和错误2 提交后输入框消失 等等错误，明明写的一样却error，然后完全copy下来后就bingo了
def login(request):
	if request.session.get('is_login',None):
		return redirect("/index/")
	if request.method == "POST":
		login_form = forms.UserForm(request.POST)
		print("login_form", login_form)
		message = "请检查填写的内容！"
		if login_form.is_valid():
			username1 = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			print('user_data:', username1, password) # NOPO
			try:
				user = models.User.objects.get(username=username1)
				print("try 里的user：",user)
				print("测试if的条件是否成立：", user.password, password)
				if user.password == password:
					print("user.id和user.name", user.id, user.username)
					request.session['is_login'] = True
					request.session['user_id'] = user.id
					request.session['user_name'] = user.username
					return redirect('/index/')
				else:
					message = "密码不正确！"
			except:
				message = "用户不存在！"
		return render(request, 'login/login.html', locals())

	login_form = forms.UserForm()
	return render(request, 'login/login.html', locals())


	
def register(request):
	#登录状态不允许注册
	if request.session.get('is_login', None):
		return redirect('/index/')
	if request.method == 'POST':
		register_form = forms.RegisterForm(request.POST)
		message = "所有内容均需填写！"
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			password1 = register_form.cleaned_data['password1']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			try:
				same_name = models.User.objects.get(username = username)
			except:
				same_name = False
			try:
				same_email = models.User.objects.get(email_address = email)
			except:
				same_email = False
			if same_name:
				message = "用户名已存在"
				return render(request, 'login/register.html', locals())
			if same_email:
				message = '该邮箱已注册'
				return render(request, 'login/register.html', locals())
			if password1 != password2:
				message = "密码不一致"
				return render(request, 'login/register.html', locals())			
			# 一切正常的情况下
			new_user = models.User()
			new_user.username = username
			new_user.password = password1
			new_user.email_address = email
			new_user.save()
			
			code = make_confirm_string(new_user)
			send_email(email, code)
			
			message = "注册成功，现在您可以登陆了"
			login_form = forms.UserForm()
			return render(request, "login/login.html",locals())
	register_form = forms.RegisterForm()
	return render(request, 'login/register.html', locals())


def logout(request):
	if not request.session.get('is_login', None):
		return redirect("/index/")
	request.session.flush()
	# 或者使用下面的方法
	# del request.session['is_login']
	# del request.session['user_id']
	# del request.session['user_name']
	return redirect("/index/")
	
def hash_code(s, salt='mysite'):
	h= hashlib.sha256()
	s += salt
	h.update(s.encode())
	return h.hexdigest()

def make_confirm_string():
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	code = hash_code(user.name, now)
	models.ConfirmString.objects.create(code=code, user=user)
	return code

def send_email(email, code):
	from django.core.mail import EmailMultiAlternatives
	
	subject = '来自www.liujiangblog.com的注册确认邮件'
	
	text_content = '''感谢注册www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
	html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.liujiangblog.com</a>，\
                    这里是刘江的博客和教程站点，专注于Python和Django技术的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)
	msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()