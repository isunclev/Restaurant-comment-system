__author__ = 'lynn'
__date__ = '2020/5/21 11:56'
from django.urls import re_path
from . import views

app_name = 'users'
urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
]