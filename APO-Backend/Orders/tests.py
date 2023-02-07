from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Catalogue.models import ProductCategory, Discount, Product
from .models import ShoppingSession, Cart, Order, PaymentDetails

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

    def tearDown(self) -> None:
        self.account.delete()

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


class CartTest(APITestCase):
    """
    1. Tests if a Cart is created
    2. Tests if a Cart query returns a queryset
    """

    def setUp(self) -> None:
        self.url = reverse("cart")
        self.account = Account.objects.create(email="test@gmail.com", password="testPass26648")
        self.session = ShoppingSession.objects.create(account=self.account, total="12")
        self.category = ProductCategory.objects.create(name="test category 0001")
        self.discount = Discount.objects.create(name="test discount", discount_percent="20", active=True)
        self.product = Product.objects.create(
            name="test product",
            description="test description",
            category=self.category,
            SKU="0183e78tqwgduv837t12823",
            price="1234.00",
            discount=self.discount
        )

    def tearDown(self) -> None:
        self.account.delete()
        self.session.delete()
        self.category.delete()
        self.discount.delete()
        self.product.delete()

    def test_cart_created_successfully(self):
        payload = {
            "shopping_session": self.session.pk,
            "products": [self.product.pk],
            "quantity": "10",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(Cart.objects.get().shopping_session, self.session)
        self.assertEqual(Cart.objects.get().products.count(), 1)
        self.assertEqual(Cart.objects.get().quantity, "10")

    def test_cart_creation_fails_on_invalid_data(self):
        payload = {
            "shopping_session": self.session.pk,
            "quantity": "10",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Cart.objects.count(), 0)

    def test_cart_query_returns_queryset(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cart.objects.count(), 0)


class OrderTest(APITestCase):
    """
    1. Tests if an Order is created
    2. Tests if an Order query returns a queryset
    """

    def setUp(self) -> None:
        self.url = reverse("orders")
        self.account = Account.objects.create(email="testing@gmail.com", password="testPass26648")
        self.category = ProductCategory.objects.create(name="test category 0001234")
        self.discount = Discount.objects.create(name="test discount", discount_percent="20", active=True)
        self.product = Product.objects.create(
            name="test product",
            description="test description",
            category=self.category,
            SKU="0183e78tqwgduv837t12823",
            price="1234.00",
            discount=self.discount
        )

    def tearDown(self) -> None:
        self.account.delete()
        self.category.delete()
        self.discount.delete()
        self.product.delete()

    def test_order_created_successfully(self):
        payload = {
            "account": self.account.pk,
            "products": [self.product.pk],
            "total": "100",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().account, self.account)
        self.assertEqual(Order.objects.get().products.count(), 1)
        self.assertEqual(Order.objects.get().total, "100")

    def test_order_creation_fails_on_invalid_data(self):
        payload = {
            "account": self.account.pk,
            "total": "100",
        }

        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 0)

    def test_order_query_returns_queryset(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 0)


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
