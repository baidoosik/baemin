from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [

    url(r'^index/$',index_view,name='index'),
    url(r'^baemin/(?P<pk>\d+)/new/',order_view,name='order'),
]