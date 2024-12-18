from django import forms


class CreateOrderForm(forms.Form):
    """
    Форма для создания заказа, включает в себя поля для имени, фамилии,
    номера телефона, выбора доставки и способа оплаты.
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_address = forms.CharField(required=False)

    PAYMENT_CHOICES = [
        ('card', 'Оплата картой'),
        ('cash', 'Наличными/картой при получении')
    ]
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
    )


    def clean_phone_number(self):
        """
        Валидация номера телефона: он должен содержать только цифры и
        иметь длину ровно 10 символов.
        """
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры')

        # Проверка на длину
        if len(data) != 10:
            raise forms.ValidationError("Неверный формат номера")
        return data
