from django.urls import path

from .views import *

urlpatterns = [
    path("", AccountRegistrationView.as_view(), name="accounts"),
    path("<int:pk>/", AccountDetailView.as_view(), name="accounts_detail"),
    path("account_address/", CustomerAddressView.as_view(), name="accounts_address"),
    path("account_address/<int:pk>/", CustomerAddressDetailView.as_view(), name="accounts_address_detail"),
    path("account_payments/", CustomerPaymentView.as_view(), name="accounts_payment"),
    path("account_payments/<int:pk>/", CustomerPaymentDetailView.as_view(), name="accounts_payment_detail"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail")
]
