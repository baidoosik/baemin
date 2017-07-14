from django.conf.urls import url,include
from . import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns =[
    url(r'^login/$',auth_views.login,name='login',kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$',auth_views.logout,name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^signup/$',views.signup,name='signup'),
]