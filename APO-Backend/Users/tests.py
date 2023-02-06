from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Account, CustomerAddress, CustomerPayment


# Create your tests here.
class AccountTests(APITestCase):

    def setUp(self):
        self.payload = {
            "email": "testAccount@gmail.com",
            "password": "testcustomerpass"
        }

    def tearDown(self):
        self.payload = None

    def test_create_account(self):
        """
        Make sure that we can create a new Account and save to database
        """
        url = reverse('accounts')

        response = self.client.post(url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().email, "testAccount@gmail.com")
        self.assertEqual(Account.objects.get().role, "Customer")
        self.assertEqual(Account.objects.get().is_active, True)
        self.assertEqual(Account.objects.get().is_staff, False)

        # Test if user is added in Customer Group
        user = Account.objects.get()
        in_customer_group = user.groups.filter(name="Customers").exists()
        self.assertEqual(in_customer_group, True)

    def test_get_accounts(self):
        """
        Make sure that we can create a new Account and save to database
        """
        url = reverse('accounts')

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.count(), 0)


class CustomerAddressTest(APITestCase):
    def setUp(self):
        self.account = Account.objects.create_user(email="test@gmail.com", password="testPassword1123")

    def tearDown(self):
        self.account.delete()

    def test_customer_address_created(self):
        """
        Test if a customer address is created successfully on providing valid data
        """
        url = reverse('accounts_address')
        payload = {
            "account_id": self.account.pk,
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
        url = reverse('accounts_address')
        payload = {
            "account_id": self.account.pk,
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
        url = reverse('accounts_address')

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomerAddress.objects.count(), 0)


class CustomerPaymentTest(APITestCase):
    """
    Tests if the Customer Payment is created and returned successfully
    """

    def setUp(self) -> None:
        self.account = Account.objects.create_user(
            email="test@gmail.com",
            password="verytastypassword"
        )

    def tearDown(self) -> None:
        self.account.delete()

    def test_customer_payment_created(self):
        url = reverse("accounts_payment")
        payload = {
            "account_id": self.account.pk,
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
        url = reverse("accounts_payment")
        payload = {
            "account_id": self.account.pk,
            "payment_type": "Mobile-Pa",
            "provider": "M-Pesa",
            "account_no": "254711111134",
            "expiry": ""
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomerPayment.objects.count(), 0)
