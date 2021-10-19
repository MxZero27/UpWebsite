from django.contrib import admin

from .models import Products
from .models import Images
# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = Images

@admin.register(Products)
class CategoryAdmin(admin.ModelAdmin):
        list_display = ['Name','Saleprice', 'Stock','Active','Created', 'SoldCount']
        list_filter = ['Stock', 'Active']
        list_editable = ['Saleprice', 'Stock', 'SoldCount']
        inlines = [PostImageAdmin]

@admin.register(Images)
class CategoryAdmin(admin.ModelAdmin):
        list_display = ['Products', ]
