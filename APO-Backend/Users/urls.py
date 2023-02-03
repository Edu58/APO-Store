from django.urls import path

from .views import *

urlpatterns = [
    path("customers/", CustomerRegistration.as_view(), name="customers")
]
