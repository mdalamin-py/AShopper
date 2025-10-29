from .models import Cart, OrderPlacement

def cart_count(request):
    """
    Context processor to add cart count and order count to all templates
    """
    cart_count = 0
    order_count = 0

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
        order_count = OrderPlacement.objects.filter(user=request.user).count()

    return {'cart_count': cart_count, 'order_count': order_count}
