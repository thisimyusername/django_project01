from django.conf.urls import include, url
from django.contrib import admin
from login import views
from django.conf.urls import include


urlpatterns = [
    # Examples:
    # url(r'^$', 'mylogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/', views.login),
	url(r'^index/', views.index),
	url(r'^register/', views.register),
	url(r'^logout/', views.logout),
	url(r'^captcha', include('captcha.urls')),
]
