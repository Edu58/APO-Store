from django.contrib.auth import get_user_model
from django.db import models

from Catalogue.models import Product


# Create your models here.
class ShoppingSession(models.Model):
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.CharField(max_length=10, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.total


class Cart(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.CharField(max_length=10, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.quantity


class Order(models.Model):
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    address = models.CharField(max_length=250, null=False, blank=False)
    total = models.CharField(max_length=100, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.total
