from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView, status, Response

from .models import Customer
from .serializers import CustomerSerializer


# Create your views here.
class CustomerRegistration(APIView):
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
