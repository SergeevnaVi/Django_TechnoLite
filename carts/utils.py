from carts.models import Cart


def get_user_carts(request):
    # Если пользователь авторизован, фильтруем корзины по полю 'user' (связанное с пользователем)
    # Метод select_related загружает связанные объекты 'product' в одном SQL-запросе для оптимизации
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')  # сокращаем кол-во sql-запросов

    # Если пользователь не авторизован, проверяем наличие session_key (если он ещё не существует)
    # Если session_key отсутствует, создаём новый сессионный ключ
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')  # сокращаем кол-во sql-запросов