from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Products
from .utils import q_search


def catalog(request, category_slug=None):
    """
    Отображает каталог товаров с возможностью фильтрации, поиска и сортировки.
    """
    # Получаем параметры из строки запроса
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    # Фильтрация товаров по категории, поисковому запросу или отображение всех товаров
    if category_slug == 'vse-tovary':
        products = Products.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = Products.objects.filter(category__slug=category_slug)

    # Применение фильтра по скидке
    if on_sale:
        products = products.filter(discount__gt=0)

    # Применение сортировки
    if order_by and order_by != 'default':
        products = products.order_by(order_by)

    # Разбиение списка товаров на страницы
    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    # Подготовка данных для шаблона
    context = {
        'title': 'TechnoLite - Главная',
        'products': current_page,
        'slug_url': category_slug
    }

    return render(request, 'products/catalog.html', context)


def product(request, product_slug):
    """
    Отображает подробную информацию о товаре.
    """
    # Получение объекта товара по его слагу
    product = Products.objects.get(slug=product_slug)

    # Подготовка данных для шаблона
    context = {
        'product': product
    }

    return render(request, 'products/product.html', context=context)
