from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Catalogue.models import ProductCategory, Product, Discount
from Checkout.models import PaymentDetails
from Orders.models import Order
from Users.models import Account


# Create your tests here.
class PaymentDetailsTest(APITestCase):
    """
    1. Tests if Payment Details are saved
    2. Tests if a Payment Details query returns a queryset
    """

    def setUp(self) -> None:
        self.url = reverse("payment_details")
        self.account = Account.objects.create(email="testings@gmail.com", password="testPass26648")
        self.category = ProductCategory.objects.create(name="test category 0s001234")
        self.discount = Discount.objects.create(name="test discount", discount_percent="20", active=True)
        self.product = Product.objects.create(
            name="test product",
            description="test description",
            category=self.category,
            SKU="0183e78tqwgduv837t12823",
            price="1234.00",
            discount=self.discount
        )
        self.order = Order.objects.create(
            account=self.account,
            total="100"
        )
        products = Product.objects.filter(name="test product")
        # Fixes Direct Assignment to a reverse side of a many-to-many set is prohibited ERROR
        self.order.products.set(products)

    def tearDown(self) -> None:
        self.account.delete()
        self.category.delete()
        self.discount.delete()
        self.product.delete()
        self.order.delete()

    def test_payment_details_created_successfully(self):
        payload = {
            "order": self.order.pk,
            "amount": "1000.383",
            "provider": "M-Pesa",
            "transaction_ID": "2rsfdyv7827281uw1"
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PaymentDetails.objects.count(), 1)
        self.assertEqual(PaymentDetails.objects.get().order, self.order)
        self.assertEqual(PaymentDetails.objects.get().amount, "1000.383")
        self.assertEqual(PaymentDetails.objects.get().transaction_ID, "2rsfdyv7827281uw1")

    def test_payment_details_creation_fails_on_invalid_data(self):
        # Missing required Order field
        payload = {
            "amount": "1000.383",
            "provider": "M-Pesa",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PaymentDetails.objects.count(), 0)

    def test_payment_details_query_returns_queryset(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PaymentDetails.objects.count(), 0)
