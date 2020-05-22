__author__ = 'lynn'
__date__ = '2020/5/21 11:18'
from django.urls import path, re_path
from . import views

# namespace
app_name = 'myrestaurants'
urlpatterns = [
    # 查看餐厅列表
    path('', views.RestaurantList.as_view(), name='restaurant_list'),

    # 查看餐厅详情
    re_path(r'^restaurant/(?P<pk>\d+)/$', views.RestaurantDetail.as_view(), name='restaurant_detail'),

    # 创建餐厅
    re_path(r'^restaurant/create/$', views.RestaurantCreate.as_view(), name='restaurant_create'),

    # 编辑餐厅详情
    re_path(r'^restaurant/(?P<pk>\d+)/edit/$', views.RestaurantEdit.as_view(), name='restaurant_edit'),

    # 创建菜品
    re_path(r'^restaurant/(?P<pk>\d+)/dishes/create/$', views.DishCreate.as_view(), name='dish_create'),

    # 编辑菜品
    re_path(r'^restaurant/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$', views.DishEdit.as_view(), name='dish_edit'),

    # 查看菜品信息
    re_path(r'^restaurant/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$', views.DishDetail.as_view(), name='dish_detail'),

    # 创建餐厅评论
    re_path(r'^restaurant/(?P<pk>\d+)/reviews/create/$', views.review_create, name='review_create'),
]
