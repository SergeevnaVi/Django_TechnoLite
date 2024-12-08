from django.shortcuts import render, redirect
from products.models import Products
from carts.models import Cart

# добавление и удаление будет производиться по slug товара
def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    # отвечает за то с какой страницы мы сюда попали
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    pass

def cart_remove(request, product_slug):
    pass
