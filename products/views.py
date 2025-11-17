from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Cart

def get_cart_count(request):
    try:
        return Cart.objects.count()
    except:
        return 0

# 🏠 Homepage (shows all products)
def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products, 'cart_count': get_cart_count(request)})


# 🛒 Add item to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


# 🧾 View cart
def view_cart(request):
    cart_items = Cart.objects.all()
    total = sum(item.total() for item in cart_items)
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total': total})


# ❌ Remove item from cart
def remove_from_cart(request, product_id):
    item = get_object_or_404(Cart, product_id=product_id)
    item.delete()
    return redirect('view_cart')


# 💳 Checkout
def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/checkout.html', {'product': product, 'cart_count': get_cart_count(request)})


# ✅ Confirm purchase
def confirm_purchase(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/thank_you.html', {'product': product, 'cart_count': get_cart_count(request)})


# 💳 Payment page
def payment_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/payment_page.html', {'product': product, 'cart_count': get_cart_count(request)})
