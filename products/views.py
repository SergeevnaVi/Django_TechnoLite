from django.shortcuts import render, get_list_or_404
from .models import Products

def catalog(request, category_slug):

    if category_slug == 'vse-tovary':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=category_slug)

    context = {
        'title': 'TechnoLite - Главная',
        'products': products,
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)