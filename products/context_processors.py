from .models import Cart

def cart_count(request):
    """Makes cart_count available globally in all templates."""
    try:
        count = Cart.objects.count()
    except:
        count = 0
    return {'cart_count': count}
