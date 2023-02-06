from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Customer, CustomerAddress, CustomerPayment


# Create your tests here.
class CustomerTests(APITestCase):

    def setUp(self):
        self.payload = {
            "email": "testcustomer@gmail.com",
            "password": "testcustomerpass"
        }

    def tearDown(self):
        self.payload = None

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


class CustomerAddressTest(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(email="test@gmail.com", password="testPassword1123")

    def tearDown(self):
        self.customer.delete()

    def test_customer_address_created(self):
        """
        Test if a customer address is created successfully on providing valid data
        """
        url = reverse('customer_address')
        payload = {
            "user_id": self.customer.pk,
            "address_line1": "test place",
            "city": "Test City",
            "postal_code": "P.O Box 0111-2000",
            "country": "Kenya",
            "telephone": "254711111111"
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomerAddress.objects.get().city, "Test City")
        self.assertEqual(CustomerAddress.objects.get().postal_code, "P.O Box 0111-2000")
        self.assertEqual(CustomerAddress.objects.get().country, "Kenya")
        self.assertEqual(CustomerAddress.objects.get().telephone, "254711111111")

    def test_create_customer_address_fails_on_invalid_data(self):
        """
        Test of create customer address fails on providing invalid data
        """
        url = reverse('customer_address')
        payload = {
            "user_id": self.customer.pk,
            "address_line1": "test place",
            "country": "Kenya",
            "telephone": "254711111111"
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_customer_addresses(self):
        """
        Tests if a list of customer addresses is returned
        """
        url = reverse('customer_address')

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomerAddress.objects.count(), 0)


class CustomerPaymentTest(APITestCase):
    """
    Tests if the Customer Payment is created and returned successfully
    """

    def setUp(self) -> None:
        self.customer = Customer.objects.create_user(
            email="test@gmail.com",
            password="verytastypassword"
        )

    def tearDown(self) -> None:
        self.customer.delete()

    def test_customer_payment_created(self):
        url = reverse("customer_payment")
        payload = {
            "user_id": self.customer.pk,
            "payment_type": "Mobile Payment",
            "provider": "M-Pesa",
            "account_no": "254711111134",
            "expiry": ""
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomerPayment.objects.count(), 1)
        self.assertEqual(CustomerPayment.objects.get().payment_type, "Mobile Payment")
        self.assertEqual(CustomerPayment.objects.get().provider, "M-Pesa")
        self.assertEqual(CustomerPayment.objects.get().expiry, '')

    def test_customer_payment_creation_fails_on_invalid_data(self):
        url = reverse("customer_payment")
        payload = {
            "user_id": self.customer.pk,
            "payment_type": "Mobile-Pa",
            "provider": "M-Pesa",
            "account_no": "254711111134",
            "expiry": ""
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomerPayment.objects.count(), 0)
