from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserLoginForm


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
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'TechnoLite - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'TechnoLite - Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'TechnoLite - Личный кабинет'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    pass