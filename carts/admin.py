from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # Определяем поля, которые будут отображаться в списке
    list_display = ['user_display', 'product', 'quantity', 'created_timestamp']

    # Определяем фильтры для списка
    list_filter = ['created_timestamp', 'user', 'product__name']

    def user_display(self, obj):
        """
        Метод для отображения имени пользователя в корзине.
        Если пользователя нет, возвращается строка 'Анонимный пользователь'.
        """
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'
