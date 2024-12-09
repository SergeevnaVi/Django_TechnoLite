from django.urls import path
from main import views

# Устанавливаем пространство имён для приложения, чтобы избежать конфликтов с другими приложениями
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('delivery-and-payment/', views.delivery_and_payment, name='delivery_and_payment'),
    path('contact-info/', views.contact_info, name='contact_info'),

]