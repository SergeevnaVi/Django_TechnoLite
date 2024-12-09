from django.contrib import admin
from products.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления категориями продуктов.

    Поле 'slug' автоматически заполняется на основе поля 'name', что упрощает создание
    читаемых и уникальных URL-адресов для каждой категории.
    """
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления продуктами.

    Поле 'slug' автоматически заполняется на основе поля 'name', что упрощает создание
    читаемых и уникальных URL-адресов для каждого продукта.

    Дополнительные настройки:
    - list_display: определяет, какие поля будут отображаться в списке товаров в админ-панели.
    - search_fields: позволяет искать товары по имени и описанию.
    - list_filter: позволяет фильтровать товары по скидке, количеству и категории.
    """
    prepopulated_fields = {'slug': ('name',)}

    list_display = ['name', 'quantity', 'price', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
