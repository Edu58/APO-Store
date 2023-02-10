from django.urls import path

from .views import *

urlpatterns = [
    path("reviews/", ProductsReviewView.as_view(), name="product_reviews"),
    path("reviews/<int:pk>/", ProductReviewDetailView.as_view(), name="product_reviews_detail")
]
