from django.db import models

# login/models.py
class User(models.Model):
	username = models.CharField(max_length=128)
	password = models.CharField(max_length=256)
	email_address = models.EmailField(unique=True)
	gender = (
		("male", '男'),
		("female", '女'),
	)
	register_date = models.DateTimeField(auto_now_add=True)
	has_confirmed = models.BooleanField(default=False)
	
	def __str__(self):
		return self.username
	
	class Meta:
		ordering = ["-register_date"]
		verbose_name = "用户1"
		verbose_name_plural = "用户"
		
class ConfirmString(models.Model):
	code = models.CharField(max_length=256)
	user = models.OneToOneField('User')
	register_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.user.name + ": " + self.code
	
	class Meta:
		ordering = ["-register_date"]
		verbose_name = "确认码"
		verbose_name_plural = "确认码"
		