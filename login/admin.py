from django.contrib import admin
from login.models import User
# Register your models here.
from login.models import ConfirmString
class DecadeEmailListFilter(admin.SimpleListFilter):
	# 提供一个标题
	title = '邮箱'
	
	# 用于URL查询的参数
	parameter_name = 'email_address'
	
	def lookups(self, request, model_admin):
		"""
		返回一个二维元组。每个元组的第一个元素是用于URL查询的真实值，
		这个值会被self.value()方法获取，并作为queryset方法的选择条件。
		第二个元素则是刻度的显示在admin页面右边侧栏的过滤选项。
		"""
		return (
			('@163.com', ('163邮箱')),
			('@sina.com', ('新浪邮箱')),
			('@qq.com', ('QQ邮箱')),
			('@126.com', ('126邮箱')),
			('@gmail.com', ('谷歌邮箱')),
			('@tom.com', ('TOM邮箱')),
		)
	def queryset(self, request, queryset):
		"""
		根据self.value()方法获取的条件值的不同执行具体的查询操作。
		并返回相应的结果。
		"""
		if self.value() == '@163.com':
			return queryset.filter(email_address.find('@163.com'))
		if self.value() == '@sina.com':
			return queryset.filter(email_address.find('@sina.com'))
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email_address','register_date','password')
	date_hiererchy = 'register_date'
	fieldsets = [
		(None,{
			'fields':['username','password'],
		}),
		('Other',{
			'fields':['email_address'],
			'classes':['collapse'],
		}),
	]
	list_filter = ('register_date',DecadeEmailListFilter)

admin.site.register(ConfirmString)