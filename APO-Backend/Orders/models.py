from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class ShoppingSession(models.Model):
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.CharField(max_length=10, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.total
