from django.contrib.auth import get_user_model
from django.db import models

from Catalogue.models import Product


# Create your models here.
class ShoppingSession(models.Model):
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.CharField(max_length=10, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.total


class Cart(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.CharField(max_length=10, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quantity


class Order(models.Model):
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.CharField(max_length=100, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.total


class PaymentDetails(models.Model):
    class Status(models.TextChoices):
        PAID = "Paid", "Paid"
        NOT_PAID = "Not Paid", "NOt Paid"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100, default=0)
    provider = models.CharField(max_length=15, null=False, blank=False)
    transaction_ID = models.CharField(max_length=100, null=False, blank=True, unique=True, db_index=True)
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.NOT_PAID)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
