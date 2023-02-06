from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ProductCategory


# Create your tests here.
class ProductTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('product_category')

    def tearDown(self) -> None:
        ProductCategory.objects.all().delete()

    def test_product_category_created(self):
        payload = {
            "name": "test category",
            "description": "Just a simple description is enough."
        }
        response = self.client.post(self.url, payload, format=None)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductCategory.objects.count(), 1)

    def test_product_category_creation_fails_on_invalid_data(self):
        payload = {
            "description": "Just a simple description is enough."
        }
        response = self.client.post(self.url, payload, format=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ProductCategory.objects.count(), 0)

    def test_product_category_returns_objects(self):
        response = self.client.get(self.url, format=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
