from django.urls import path

from .views import *

urlpatterns = [
    path("payment_details/", PaymentDetailsView.as_view(), name="payment_details"),
    path("payment_details/<int:pk>/", PaymentDetailsDetailView.as_view(), name="payment_details_detail"),
]
