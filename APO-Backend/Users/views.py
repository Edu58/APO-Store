from django.views.decorators.vary import vary_on_headers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView, status, Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Account, CustomerAddress, CustomerPayment, Profile
from .serializers import AccountSerializer, CustomerAddressSerializer, CustomerPaymentSerializer, ProfileSerializer

# Celery tasks
from .tasks import send_welcome_email


# Create your views here.
class AccountRegistrationView(APIView, PageNumberPagination):
    """
    1. Create a new Account
    2. Get the first 10 Accounts
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            200: AccountSerializer(many=True)
        },
        operation_description='Returns a list of the first 10 Accounts'
    )
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(cache_page(60 * 5))
    def get(self, request, format=None, *args, **kwargs):
        accounts = Account.objects.all()

        paginated_accounts = self.paginate_queryset(accounts, request, view=self)
        account_serializer = AccountSerializer(paginated_accounts, many=True)
        return Response(
            data=account_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=AccountSerializer,
        operation_description='Creates a new Account'
    )
    def post(self, request, *args, **kwargs):
        account_serializer = AccountSerializer(data=request.data)

        if account_serializer.is_valid():
            account_serializer.save()

            # Send welcome email on successful registration
            send_welcome_email.delay(account_serializer.data.get("email"))
            return Response(
                data=account_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=account_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class AccountDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CustomerAddressView(APIView, PageNumberPagination):
    """
    1. Creates a Customer Address
    2. Get a list of the first 10 Customer Addresses
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Returns a list of the first 10 Customer Addresses"
    )
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(cache_page(60 * 5))
    def get(self, request, format=None, *args, **kwargs):
        customer_addresses = CustomerAddress.objects.all()

        paginated_customer_addresses = self.paginate_queryset(customer_addresses, request, view=self)
        customer_addresses_serializer = CustomerAddressSerializer(paginated_customer_addresses, many=True)

        return Response(
            data=customer_addresses_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=CustomerAddressSerializer,
        operation_description="Creates a new Customer Address"
    )
    def post(self, request, format=None, *args, **kwargs):
        customer_serializer = CustomerAddressSerializer(data=request.data)

        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(
                data=customer_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=customer_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomerAddressDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer


class CustomerPaymentView(APIView, PageNumberPagination):
    """
    1. Creates a Customer Payment
    2. Get a list of the first 10 Customer Payments objects
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Returns a list of the first 10 Customer Payments"
    )
    def get(self, request, format=None, *args, **kwargs):
        customer_payments = CustomerPayment.objects.all()

        paginated_customer_payments = self.paginate_queryset(customer_payments, request, view=self)
        customer_payments_serializer = CustomerPaymentSerializer(paginated_customer_payments, many=True)
        return Response(
            data=customer_payments_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=CustomerPaymentSerializer,
        operation_description="Created a Customer Payment and saves to DB"
    )
    def post(self, request, format=None, *args, **kwargs):
        customer_payment_serializer = CustomerPaymentSerializer(data=request.data)

        if customer_payment_serializer.is_valid():
            customer_payment_serializer.save()
            return Response(
                data=customer_payment_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=customer_payment_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomerPaymentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomerPayment.objects.all()
    serializer_class = CustomerPaymentSerializer


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
