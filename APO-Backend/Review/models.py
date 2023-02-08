from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from Catalogue.models import Product


# Create your models here.
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)],
        null=False,
        blank=False
    )
    comment = models.TextField(null=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating

