from django.contrib import admin

from .models import ShoppingSession, Order, PaymentDetails, Cart

# Register your models here.
admin.site.register([
    ShoppingSession,
    Order,
    PaymentDetails,
    Cart
])
