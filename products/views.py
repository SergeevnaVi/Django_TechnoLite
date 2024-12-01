from django.shortcuts import render
from .models import Products

def catalog(request):

    products = Products.objects.all()

    context = {
        'title': 'TechnoLite - Главная',
        'products': products,
    }
    return render(request, 'products/catalog.html', context)


def product(request):
    return render(request, 'products/product.html')