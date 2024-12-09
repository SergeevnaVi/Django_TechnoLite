from django.contrib.postgres.search import SearchVector
from products.models import Products


"""
Функция для выполнения поиска в базе данных.

Если переданный запрос является числом, и длина его не превышает 5 символов, 
то выполняется поиск по полю `id` товаров. В противном случае используется 
полноконтекстный поиск (PostgreSQL SearchVector) по полям `name` и `description`.
"""
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    return Products.objects.annotate(
        search=SearchVector("name", "description"),
    ).filter(search=query)


