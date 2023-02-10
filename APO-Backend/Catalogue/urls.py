from django.urls import path

from .views import *

urlpatterns = [
    path("product_category/", ProductCategoryView.as_view(), name="product_category"),
    path("product_category/<int:pk>/", ProductCategoryDetailView.as_view(), name="product_category_detail"),
    path("discount/", DiscountView.as_view(), name="discount"),
    path("discount/<int:pk>/", DiscountDetailView.as_view(), name="discount_detail"),
    path("products/", ProductView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail")
]
