from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, db_index=True)
    description = models.TextField(null=False, blank=True)
    discount_percent = models.CharField(max_length=10, default=0)
    active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, db_index=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="photos/products/")
    description = models.TextField(null=False, blank=True)
    color = models.CharField(max_length=250, null=False, blank=True)
    size = models.CharField(max_length=5, null=False, blank=True)
    SKU = models.CharField(max_length=250, null=False, blank=False, unique=True, db_index=True)
    price = models.CharField(max_length=250, default=0)
    quantity = models.IntegerField(default=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
