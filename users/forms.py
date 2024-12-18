from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):
    """
    Форма для аутентификации пользователя.

    Используется для проверки введенных данных (имя пользователя и пароль) при входе.
    В этой форме используются стандартные поля 'username' и 'password'.
    """
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя.

    Включает поля для ввода имени, фамилии, имени пользователя, email и паролей.
    Также осуществляется проверка на совпадение пароля и подтверждения пароля.
    """
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2'
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    """
    Форма для изменения профиля пользователя.

    Позволяет пользователю изменить аватар, имя, фамилию, имя пользователя и email.
    """
    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()