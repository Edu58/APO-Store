from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView, status, Response

from .models import Customer, CustomerAddress
from .serializers import CustomerSerializer, CustomerAddressSerializer


# Create your views here.
class CustomerRegistrationView(APIView):
    """
    1. Create a new Customer
    2. Get the first 10 customers
    """

    @swagger_auto_schema(
        responses={
            200: CustomerSerializer(many=True)
        },
        operation_description='Returns a list of the first 10 customers'
    )
    def get(self, format=None, *args, **kwargs):
        customers = Customer.objects.all()[:10]
        customer_serializer = CustomerSerializer(customers, many=True)
        return Response(
            data=customer_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=CustomerSerializer,
        operation_description='Creates a new Customer'
    )
    def post(self, request, *args, **kwargs):
        customer_serializer = CustomerSerializer(data=request.data)

        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(
                data=customer_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=customer_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class CustomerAddressView(APIView):
    """
    1. Creates a Customer Address
    2. Get a list of the first 10 Customer Addresses
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the first 10 Customer Addresses"
    )
    def get(self, format=None, *args, **kwargs):
        customer_addresses = CustomerAddress.objects.all()[:10]
        customer_addresses_serializer = CustomerAddressSerializer(customer_addresses, many=True)

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
