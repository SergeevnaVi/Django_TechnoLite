from carts.models import Cart


def get_user_carts(request):
    """
    Получает корзины пользователя на основе авторизации или сессионного ключа.

    Если пользователь авторизован, фильтруются корзины по полю 'user'.
    Для авторизованных пользователей используется метод select_related для оптимизации запросов,
    чтобы сразу загрузить связанные товары.

    Если пользователь не авторизован, проверяется наличие session_key.
    Если ключ отсутствует, создается новый сессионный ключ, и корзины фильтруются по этому ключу.
    """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')

    if not request.session.session_key:
        request.session.create()
        
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')
