from django.urls import path

from .views import *

urlpatterns = [
    path("accounts/", AccountRegistrationView.as_view(), name="accounts"),
    path("accounts/<int:pk>/", AccountDetailView.as_view(), name="accounts_detail"),
    path("accounts/account_address/", CustomerAddressView.as_view(), name="accounts_address"),
    path("accounts/account_address/<int:pk>/", CustomerAddressDetailView.as_view(), name="accounts_address_detail"),
    path("accounts/account_payments/", CustomerPaymentView.as_view(), name="accounts_payment"),
    path("accounts/account_payments/<int:pk>/", CustomerPaymentDetailView.as_view(), name="accounts_payment_detail")
]
