from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Cart
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Buy Now
    path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),

    # Checkout + Payment
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment_page, name='payment_page'),
    path('confirm/', views.confirm_purchase, name='confirm_purchase'),
]
