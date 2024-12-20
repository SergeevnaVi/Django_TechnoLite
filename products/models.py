from django.db import models


class Categories(models.Model):
    """
    Модель категории товара в магазине. Содержит информацию о названии категории
    и уникальном URL-идентификаторе (slug).
    """
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    """
    Модель товара, содержащая информацию о названии, производителе, цене, описании и других характеристиках.
    Связан с категорией, к которой относится товар.
    """
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    manufacturer = models.CharField(max_length=55, blank=True, null=True, verbose_name='Производитель')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}. Количество - {self.quantity}'

    def display_id(self):
        """
        Возвращает уникальный идентификатор товара, отформатированный с ведущими нулями (например, 00001).
        """
        return f'{self.id:05}'

    def sell_price(self):
        """
        Рассчитывает цену товара с учетом скидки.
        Если скидка есть, применяет ее, иначе возвращает обычную цену.
        """
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price