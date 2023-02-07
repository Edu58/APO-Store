from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ShoppingSession

Account = get_user_model()


# Create your tests here.
class ShoppingSessionTest(APITestCase):
    """
    1. Tests if a shopping session is created
    2. Tests if a Shopping Session query returns a queryset
    """

    def setUp(self) -> None:
        self.url = reverse("shopping_sessions")
        self.account = Account.objects.create(email="test@gmail.com", password="testPass26648")

    def test_shopping_session_created_sucessfully(self):
        payload = {
            "account": self.account.pk,
            "total": "12",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShoppingSession.objects.count(), 1)
        self.assertEqual(ShoppingSession.objects.get().account, self.account)
        self.assertEqual(ShoppingSession.objects.get().total, "12")

    def test_shopping_session_creation_fails_on_invalid_data(self):
        payload = {
            "total": "12",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ShoppingSession.objects.count(), 0)

    def test_shopping_session_query_returns_queryset(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        