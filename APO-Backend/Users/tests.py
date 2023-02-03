from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Customer


# Create your tests here.
class CustomerTests(APITestCase):

    def setUp(self):
        self.payload = {
            "email": "testcustomer@gmail.com",
            "password": "testcustomerpass"
        }

    def test_create_customer(self):
        """
        Make sure that we can create a new customer and save to database
        """
        url = reverse('customers')

        response = self.client.post(url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().email, "testcustomer@gmail.com")
        self.assertEqual(Customer.objects.get().is_active, True)
        self.assertEqual(Customer.objects.get().is_staff, False)

    def test_get_customers(self):
        """
        Make sure that we can create a new customer and save to database
        """
        url = reverse('customers')

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.count(), 0)
