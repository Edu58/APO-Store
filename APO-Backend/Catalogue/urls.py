from django.urls import path

from .views import *

urlpatterns = [
    path("product_category/", ProductCategoryView.as_view(), name="product_category")
]
