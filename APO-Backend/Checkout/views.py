from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Checkout.models import PaymentDetails
from Checkout.serializers import PaymentDetailsSerializer


# Create your views here.
class PaymentDetailsView(APIView):
    """
    1. Creates a Payment Details Object and saves to DB
    2. Returns a list of 10 latest Payment Objects
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 Payment Details"
    )
    def get(self, format=None, *args, **kwargs):
        payment_details = PaymentDetails.objects.all()[:10]
        payment_details_serializer = PaymentDetailsSerializer(payment_details, many=True)
        return Response(
            data=payment_details_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=PaymentDetailsSerializer,
        operation_description="Creates a new Payment Detail"
    )
    def post(self, request, format=None, *args, **kwargs):
        payment_details_serializer = PaymentDetailsSerializer(data=request.data)

        if payment_details_serializer.is_valid():
            payment_details_serializer.save()
            return Response(
                data=payment_details_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=payment_details_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PaymentDetailsDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer
