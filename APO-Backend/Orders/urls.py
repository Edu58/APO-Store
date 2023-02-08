from django.urls import path

from .views import *

urlpatterns = [
    path("shopping_session/", ShoppingSessionView.as_view(), name="shopping_sessions"),
    path("cart/", CartView.as_view(), name="cart"),
    path("orders/", OrderView.as_view(), name="orders")
]
