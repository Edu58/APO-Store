from django.urls import path

from .views import *

urlpatterns = [
    path("query/<str:product_name>/", QueryProducts.as_view(), name="query_products")
]
