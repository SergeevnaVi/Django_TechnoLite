from django.contrib import admin
from orders.models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке заказов
    list_display = "order", "product", "name", "price", "quantity"

    # Параметры для поиска по заказам
    search_fields = (
        "order",
        "product",
        "name",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке заказов
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    # Параметры для поиска по заказам (по id)
    search_fields = (
        "id",
    )

    # Поля только для чтения
    readonly_fields = ("created_timestamp",)

    # Фильтрация заказов
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
    )
