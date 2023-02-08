from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Catalogue.models import Product, ProductCategory, Discount
from Users.models import Account
from .models import ProductReview


# Create your tests here.
class ProductReviewTest(APITestCase):
    """
    1. Test if the Product Review is saved successfully
    2. Tests if a products reviews are returned successfully
    """

    def setUp(self) -> None:
        self.url = reverse("product_reviews")
        self.account = Account.objects.create(email="tesztings@gmail.com", password="testPass26648")
        self.category = ProductCategory.objects.create(name="tezst category 0s001234")
        self.discount = Discount.objects.create(name="test discount", discount_percent="20", active=True)
        self.product = Product.objects.create(
            name="test product",
            description="test description",
            category=self.category,
            SKU="0183e78tqwgduv837t12823",
            price="1234.00",
            discount=self.discount
        )

    def test_product_review_created_successfully(self):
        payload = {
            "product": self.product.pk,
            "rating": 4.5,
            "comment": "Jolly Good product"
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductReview.objects.count(), 1)
        self.assertEqual(ProductReview.objects.get().product, self.product)
        self.assertEqual(ProductReview.objects.get().rating, 4.5)

    def test_product_review_creation_fails_on_invalid_data(self):
        payload = {
            "product": self.product.pk,
            "comment": "Jolly Good product"
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ProductReview.objects.count(), 0)

    def test_product_review_query_returns_queryset(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductReview.objects.count(), 0)
