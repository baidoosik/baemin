from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    url(r'^accounts/login/$',auth_views.login,
        kwargs={'template_name':'shop/login_form.html'}),
    url(r'^accounts/logout/$', auth_views.logout,
        kwargs={'next_page': 'shop/login_form.html'}),
    url(r'^index/$',index_view,name='index')
]