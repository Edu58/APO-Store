from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ProductCategory, Discount


# Create your tests here.
class ProductCategoryTest(APITestCase):
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


class DiscountTest(APITestCase):
    """
    1. Test if a Dicount object is created and saved successfully
    2. Test if a Discount queryset is returned successfully on request
    """

    def setUp(self) -> None:
        self.url = reverse('discount')

    def tearDown(self) -> None:
        Discount.objects.all().delete()

    def test_discount_created_successfully(self):
        payload = {
            "name": "test discount",
            "description": "test description",
            "discount_percent": "20",
            "active": True
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Discount.objects.count(), 1)
        self.assertEqual(Discount.objects.get().name, "test discount")
        self.assertEqual(Discount.objects.get().discount_percent, "20")
        self.assertEqual(Discount.objects.get().active, True)

    def test_create_discount_fails_on_invalid_data(self):
        payload = {
            "description": "test description",
            "active": True
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Discount.objects.count(), 0)

    def test_discount_queryset_returns_data(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Discount.objects.count(), 0)
        