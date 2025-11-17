from django.db import models
from django.utils import timezone

class Product(models.Model):
    UNIT_CHOICES = [
        ('0.5kg', '½ Kg'),
        ('1kg', '1 Kg'),
    ]

    name = models.CharField(max_length=100)
    price = models.FloatField(help_text="Price per selected unit")
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2083)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='1kg')

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.code


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sale: {self.product.name} - ${self.total_price}"


# 🛒 Cart model
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def total(self):
        return self.product.price * self.quantity
