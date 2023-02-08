from django.urls import path

from .views import *

urlpatterns = [
    path("payment_details/", PaymentDetailsView.as_view(), name="payment_details"),
]
