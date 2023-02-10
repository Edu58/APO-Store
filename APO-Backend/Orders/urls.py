from django.urls import path

from .views import *

urlpatterns = [
    path("shopping_session/", ShoppingSessionView.as_view(), name="shopping_sessions"),
    path("shopping_session/<int:pk>/", ShoppingSessionDetailView.as_view(), name="shopping_sessions_detail"),
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/<int:pk>/", CartDetailView.as_view(), name="cart_detail"),
    path("orders/", OrderView.as_view(), name="orders"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="orders_detail")
]
