from django.contrib import admin
from .models import Product, Offer, Sale


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'date')
    list_filter = ('date',)
    search_fields = ('product__name',)


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
