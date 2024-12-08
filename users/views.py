from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # наполняем данными которые ввел пользователь
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # если такой пользователь есть, то он вернет данные в переменную user
            user = auth.authenticate(username=username, password=password)
            if user:
                # проходит авторизация
                auth.login(request, user)

                #
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'TechnoLite - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)  # наполняем данными которые ввел пользователь
        if form.is_valid():
            form.save()
            # автоматически проходит авторизацию при регистрации и попадает на главный экран
            user = form.instance
            auth.login(request, user)
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

    context = {
        'title': 'TechnoLite - Личный кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))