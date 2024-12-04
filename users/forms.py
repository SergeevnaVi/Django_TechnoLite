from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


# этот класс нужен, чтобы применить валидаторы на вводимые данные (проверка на соответствие)
# бывают формы: не связанные с моделями(таблицами) и связанные с моделями
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
