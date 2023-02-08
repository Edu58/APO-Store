from django.contrib import admin

from .models import ShoppingSession, Order, Cart

# Register your models here.
admin.site.register([
    ShoppingSession,
    Order,
    Cart
])
