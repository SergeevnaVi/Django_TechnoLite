from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Products

def catalog(request, category_slug):

    page = request.GET.get('page', 1)

    if category_slug == 'vse-tovary':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'TechnoLite - Главная',
        'products': current_page,
        'slug_url': category_slug
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)