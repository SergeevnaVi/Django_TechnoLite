from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages

from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    """
    Представление для создания заказа. Доступно только авторизованным пользователям.
    """
    if request.method == 'POST':
        # Инициализация формы с данными, отправленными через POST-запрос
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                # Объединение действий в одну транзакцию для обеспечения целостности данных
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Определяем способ оплаты
                        payment_method = form.cleaned_data['payment_method']  # 'card' или 'cash'
                        is_paid = payment_method == 'card'  # True, если оплата картой, иначе False

                        # Создаем заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=(payment_method == 'cash'),  # Если 'cash', то True, если 'card' - False
                            is_paid=is_paid,  # Статус оплаты
                        )
                        # Создаем записи для каждого товара в заказе
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            # Проверка доступного количества товара
                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            # Создаем позицию в заказе
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            # Обновляем остаток товара на складе
                            product.quantity -= quantity
                            product.save()

                        # Очищаем корзину пользователя после создания заказа
                        cart_items.delete()

                        # Сообщение об успешном оформлении заказа
                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                # Обработка ошибок валидации
                messages.success(request, str(e))
                # Перенаправление обратно на страницу заказа
                return redirect('orders:create_order')
    else:
        # Если запрос GET, подставляем начальные данные из профиля пользователя
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'TechnoLite - Оформление заказа',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)
