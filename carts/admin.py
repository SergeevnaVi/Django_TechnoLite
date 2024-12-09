from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product', 'quantity', 'created_timestamp']
    list_filter = ['created_timestamp', 'user', 'product__name']

    def user_display(self, obj):
        # Если у корзины есть пользователь, показываем его имя
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'
