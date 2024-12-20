from django.http import JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from products.models import Products
from carts.models import Cart
from carts.utils import get_user_carts


def cart_add(request):
    """
    Добавляет товар в корзину.

    Для авторизованных пользователей корзина привязывается к пользователю,
    для неавторизованных — к сессионному ключу. Если товар уже есть в корзине,
    увеличивается его количество. Если нет, создается новая запись в корзине.
    """
    product_id = request.POST.get('product_id')
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        # Обработка для авторизованных пользователей
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        # Обработка для неавторизованных пользователей
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    # Получаем обновленную корзину и рендерим HTML
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts': user_cart}, request=request)

    response_data = {
        'message': 'Товар добавлен в корзину',
        'cart_items_html': cart_items_html,
    }

    return JsonResponse(response_data)

def cart_change(request):
    """
    Изменяет количество товара в корзине.
    """
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    # Получаем обновленную корзину и рендерим HTML
    user_cart = get_user_carts(request)
    context = {"carts": user_cart}
    referer = request.META.get('HTTP_REFERER')
    if reverse('orders:create_order') in referer:
        context["order"] = True

    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', context, request=request)

    response_data = {
        'message': 'Количество изменено',
        'cart_items_html': cart_items_html,
        'quantity': updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    """
    Удаляет товар из корзины.
    """
    cart_id = request.POST.get('cart_id')

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    # Получаем обновленную корзину и рендерим HTML
    user_cart = get_user_carts(request)
    context = {"carts": user_cart}
    referer = request.META.get('HTTP_REFERER')
    if reverse('orders:create_order') in referer:
        context["order"] = True
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', context, request=request)

    response_data = {
        'message': 'Товар удален',
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity,
    }

    return JsonResponse(response_data)
