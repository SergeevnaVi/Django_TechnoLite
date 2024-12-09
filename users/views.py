from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from carts.models import Cart
from orders.models import OrderItem, Order


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # наполняем данными которые ввел пользователь
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # если такой пользователь есть, то он вернет данные в переменную user
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                # проходит авторизация
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'TechnoLite - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def password(request):
    context = {
        'title': 'TechnoLite - Восстановление пароля',
        'content': 'Восстановление пароля',
        'text_on_page': 'Мы приносим извинения за временные неудобства. Пожалуйста, попробуйте позже.',
        'text_on_page2': 'Если у вас возникли вопросы, пожалуйста, свяжитесь с нашей службой поддержки.',
        'phone': '+7 (123) 456-78-90',
        'email': 'support@technolite.ru',
        'text_on_page3': 'Мы всегда готовы помочь вам. Пожалуйста, не стесняйтесь обращаться.',
    }
    return render(request, 'users/password.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)  # наполняем данными которые ввел пользователь
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            # автоматически проходит авторизацию при регистрации и попадает на главный экран
            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f'{user.username}, Вы вошли в аккаунт')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'TechnoLite - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

# Запретить доступ к контроллерам - не авторизованным пользователям
@login_required
def profile(request):
    if request.method == 'POST':
        # наполняем данными которые ввел пользователь и
        # указываем для какого пользователя будут сохранены значения (изменения) и принимать файлы
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            # автоматически проходит авторизацию при регистрации и попадает на главный экран
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user).prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('product'),
            )
        )
        .order_by('-id')
    )

    context = {
        'title': 'TechnoLite - Личный кабинет',
        'form': form,
        'orders': orders
    }
    messages.success(request, 'Ваша учетная запись обновлена')
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))

