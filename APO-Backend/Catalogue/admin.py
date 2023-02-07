from django.contrib import admin

from .models import ProductCategory, Discount, Product

# Register your models here.
admin.site.register([
    ProductCategory,
    Discount,
    Product
])
