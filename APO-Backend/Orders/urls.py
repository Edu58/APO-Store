from django.urls import path

from .views import *

urlpatterns = [
    path("shopping_session/", ShoppingSessionView.as_view(), name="shopping_sessions")
]
