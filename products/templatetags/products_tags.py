from django import template
from django.utils.http import urlencode
from products.models import Categories

register = template.Library()

@register.simple_tag()
def tags_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True) # все контекстные переменные будут доступны
def change_params(context, **kwargs):
    quare = context['request'].GET.dict()  # Получаем текущие параметры запроса в виде словаря.
    quare.update(kwargs)  # Обновляем их с учетом новых параметров, переданных через **kwargs.
    return urlencode(quare)  # Кодируем обновленный словарь в формат URL-параметров.