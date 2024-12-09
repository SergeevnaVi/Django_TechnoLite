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
        'name': 'TechnoLite',
        'title': 'TechnoLite - О нас',
        'content': 'О нас',
        'text_on_page': 'Почему выбирают нас?',
        'text1': 'Широкий ассортимент товаров.',
        'text2': 'Выгодные цены и акции для наших клиентов.',
        'text3': 'Профессиональная консультация и помощь в выборе.',
        'text4': 'Быстрая доставка по всей стране.',
        'text5': 'Гарантия качества на всю продукцию.',
        'mission': 'Наша миссия',
        'text_mission': 'Мы стремимся сделать вашу жизнь комфортнее и удобнее, предлагая технику, которая упрощает ваш быт'
                        ' и повышает его качество. Каждый клиент важен для нас, и мы всегда готовы предоставить лучший сервис.'

    }
    return render(request, 'main/about.html', context)


def delivery_and_payment(request):
    context = {
        'title': 'TechnoLite - Доставка и оплата',
        'content': 'Информация о доставке и оплате',
        'text_on_page': 'Мы предлагаем несколько удобных способов доставки и оплаты для наших клиентов. Ознакомьтесь с ними ниже:',
        'delivery_method': 'Способы доставки',
        'methods_del': 'Доставка по городу - бесплатно.',
        'methods2_del': 'Доставка за пределы города - от 500 рублей (в зависимости от расстояния).',
        'methods3_del': 'Самовывоз - бесплатно (оформите заказ на сайте, и мы подготовим ваш товар).',
        'payment_method': 'Способы оплаты',
        'methods_pay': 'Наличными при получении.',
        'methods_pay2': 'Оплата картой на сайте.',
        'methods_pay3': 'Оплата картой при получении.',
    }
    return render(request, 'main/delivery_and_payment.html', context)

def contact_info(request):
    context = {
        'name': 'TechnoLite',
        'title': 'TechnoLite - Контактная информация',
        'content': 'Контактная информация',
        'text_on_page': 'Мы всегда рады помочь вам! Свяжитесь с нами любым удобным способом:',
        'contact': 'Наши контакты',
        'phone': '+7 (123) 456-78-90',
        'email': 'support@technolite.ru',
        'address': 'ул. Примерная, дом 12, офис 34, Москва',
        'social_networks': 'Социальные сети',
    }
    return render(request, 'main/contact_info.html', context)