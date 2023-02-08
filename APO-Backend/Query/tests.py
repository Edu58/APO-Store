from django.shortcuts import reverse
from rest_framework import status
from rest_framework.serializers import ReturnList
from rest_framework.test import APITestCase


# Create your tests here.
class QueryProductsTest(APITestCase):
    """
    Test if the query_products endpoint returns a valid result
    """

    def setUp(self) -> None:
        self.url = reverse("query_products", kwargs={'product_name': 'test'})

    def test_query_products_returns_data(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(type(response.data["results"]), ReturnList)
        self.assertEqual(len(response.data["results"]), 0)
