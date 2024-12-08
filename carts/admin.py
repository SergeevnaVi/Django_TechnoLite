from django.contrib import admin

from .models import Cart


# admin.site.register(Cart)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product', 'quantity', 'created_timestamp']
    list_filter = ['created_timestamp', 'user', 'product__name']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'
