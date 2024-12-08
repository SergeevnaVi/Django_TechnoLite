from django.contrib import admin
from products.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    # для красивого оформления админ-панели товаров
    list_display = ['name', 'quantity', 'price', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
