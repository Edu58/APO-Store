from django.urls import path

from .views import *

urlpatterns = [
    path("product_category/", ProductCategoryView.as_view(), name="product_category"),
    path("discount/", DiscountView.as_view(), name="discount"),
    path("products/", ProductView.as_view(), name="products")
]
