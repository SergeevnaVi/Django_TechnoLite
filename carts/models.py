from django.db import models
from users.models import User
from products.models import Products


class CartQueryset(models.QuerySet):
    """
    Класс, расширяющий QuerySet для работы с корзинами.
    Добавляет методы для вычисления общей стоимости и количества товаров в корзине.
    """
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    """
    Модель корзины покупок, представляющая товары, добавленные в корзину пользователем.
    Хранит информацию о пользователе, товаре, количестве товаров, сессионном ключе и времени добавления.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзин(ы)'

    # Менеджер для корзины с методами подсчета
    objects = CartQueryset().as_manager()

    def products_price(self):
        """
        Метод для вычисления стоимости товара в корзине.
        """
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
