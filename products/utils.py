from django.contrib.postgres.search import SearchVector
from products.models import Products


def q_search(query):
    """
    Функция для выполнения поиска в базе данных.

    Если переданный запрос является числом, и длина его не превышает 5 символов,
    то выполняется поиск по полю `id` товаров. В противном случае используется
    полнотекстовый поиск (PostgreSQL SearchVector) по полям `name` и `description`.
    """
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    return Products.objects.annotate(
        search=SearchVector("name", "description"),
    ).filter(search=query)


