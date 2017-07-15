from django.contrib import admin
from .models import Shop,Order,Item

# Register your models here.
@admin.register(Shop)
class Shopadmin(admin.ModelAdmin):
    list_display = ['id','name','tel','addr']
    list_display_links = ['id', 'name']
    list_filter = ['name']

@admin.register(Item)
class Itemadmin(admin.ModelAdmin):
    list_display = ['id','shop','name','price']
    list_display_links = ['id', 'name']
    list_filter = ['name']

@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    list_display = ['id','shop']
    list_display_links = ['id']
    list_filter = ['user']