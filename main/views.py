from django.http import HttpResponse
from django.shortcuts import render
from products.models import Categories

def index(request):

    context = {
        'title': 'TechnoLite - Главная',
        'content': 'Магазин бытовой техники TechnoLite',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'TechnoLite - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин хороший'
    }
    return render(request, 'main/about.html', context)