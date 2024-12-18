from django.apps import AppConfig


class CartsConfig(AppConfig):
    """Конфигурация приложения 'Carts' для Django."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'
    verbose_name = 'Корзины'
