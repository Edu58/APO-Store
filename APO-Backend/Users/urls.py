from django.urls import path

from .views import *

urlpatterns = [
    path("customer/", CustomerRegistrationView.as_view(), name="customers"),
    path("customer/customer_address/", CustomerAddressView.as_view(), name="customer_address")
]
