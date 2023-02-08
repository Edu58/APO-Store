from django.db import models

from Orders.models import Order


# Create your models here.
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
