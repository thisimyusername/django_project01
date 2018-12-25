import os 
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
	send_mail(
		'来自www.xxxx.com的测试邮件',
		'欢迎访问www。liujiangblog.com，本站专注Python和Django的技术分享',
		'sanqian3qian@sina.com',
	)