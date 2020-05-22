from django.contrib import admin
from .models import Restaurant, RestaurantReview, Dish, Review

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'telephone', 'url', 'user', 'date')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'user', 'date', 'image', 'restaurant')