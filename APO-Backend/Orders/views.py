from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShoppingSession, Cart, Order, PaymentDetails
from .serializers import ShoppingSessionSerializer, CartSerializer, OrderSerializer, PaymentDetailsSerializer


# Create your views here.
class ShoppingSessionView(APIView):
    """
    1. Creates a Shopping Session
    2. Returns a list of 10 latest Shopping Sessions
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 shopping sessions"
    )
    def get(self, format=None, *args, **kwargs):
        shopping_session = ShoppingSession.objects.all()[:10]
        shopping_session_serializer = ShoppingSessionSerializer(shopping_session, many=True)
        return Response(
            data=shopping_session_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=ShoppingSessionSerializer,
        operation_description="Creates a new Shopping Session"
    )
    def post(self, request, format=None, *args, **kwargs):
        shopping_session_serializer = ShoppingSessionSerializer(data=request.data)

        if shopping_session_serializer.is_valid():
            shopping_session_serializer.save()
            return Response(
                data=shopping_session_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=shopping_session_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CartView(APIView):
    """
    1. Creates a Cart
    2. Returns a list of 10 latest Carts
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 Carts"
    )
    def get(self, format=None, *args, **kwargs):
        cart = Cart.objects.all()[:10]
        cart_serializer = ShoppingSessionSerializer(cart, many=True)
        return Response(
            data=cart_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=CartSerializer,
        operation_description="Creates a new Cart"
    )
    def post(self, request, format=None, *args, **kwargs):
        cart_serializer = CartSerializer(data=request.data)

        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(
                data=cart_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=cart_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class OrderView(APIView):
    """
    1. Creates an Order
    2. Returns a list of 10 latest Order
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 Orders"
    )
    def get(self, format=None, *args, **kwargs):
        order = Order.objects.all()[:10]
        order_serializer = ShoppingSessionSerializer(order, many=True)
        return Response(
            data=order_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=OrderSerializer,
        operation_description="Creates a new Order"
    )
    def post(self, request, format=None, *args, **kwargs):
        order_serializer = OrderSerializer(data=request.data)

        if order_serializer.is_valid():
            order_serializer.save()
            return Response(
                data=order_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=order_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


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
