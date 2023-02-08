from django.urls import path

from .views import *

urlpatterns = [
    path("reviews/", ProductsReviewView.as_view(), name="product_reviews")
]
