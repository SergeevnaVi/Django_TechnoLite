from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')  # сокращаем кол-во sql-запросов


    if not request.session.session_key:
        request.session.create()  # Создаем session_key, если его нет
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')  # сокращаем кол-во sql-запросов