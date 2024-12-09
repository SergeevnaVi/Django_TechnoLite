from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    # Путь для поиска товаров. Принимает запрос на поиск и отображает результаты
    path('search/', views.catalog, name='search'),

    # Путь для отображения списка товаров в конкретной категории.
    # Принимает slug категории и передает его в представление для отображения товаров этой категории.
    path('<slug:category_slug>/', views.catalog, name='index'),

    # Путь для отображения подробной информации о товаре.
    # Принимает slug товара и отображает его детали в отдельном представлении.
    path('product/<slug:product_slug>/', views.product, name='product'), # конвертор

]