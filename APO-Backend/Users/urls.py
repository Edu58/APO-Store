from django.urls import path

from .views import *

urlpatterns = [
    path("accounts/", AccountRegistrationView.as_view(), name="accounts"),
    path("accounts/account_address/", CustomerAddressView.as_view(), name="accounts_address"),
    path("accounts/account_payments/", CustomerPaymentView.as_view(), name="accounts_payment")
]
