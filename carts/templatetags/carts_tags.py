from django import template  # Библиотека для работы с кастомными тегами
from carts.utils import get_user_carts

# Регистрируем кастомный тег
register = template.Library()

@register.simple_tag()
def user_carts(request):
    """Тег для получения корзин пользователя."""
    return get_user_carts(request)
