from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShoppingSession, Cart, Order
from .serializers import ShoppingSessionSerializer, CartSerializer, OrderSerializer


# Create your views here.
class ShoppingSessionView(APIView, PageNumberPagination):
    """
    1. Creates a Shopping Session
    2. Returns a list of 10 latest Shopping Sessions
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 shopping sessions"
    )
    def get(self, request, format=None, *args, **kwargs):
        shopping_session = ShoppingSession.objects.all()

        paginated_shopping_session = self.paginate_queryset(shopping_session, request, self)
        shopping_session_serializer = ShoppingSessionSerializer(paginated_shopping_session, many=True)
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


class ShoppingSessionDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


class CartView(APIView, PageNumberPagination):
    """
    1. Creates a Cart
    2. Returns a list of 10 latest Carts
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 Carts"
    )
    def get(self, request, format=None, *args, **kwargs):
        cart = Cart.objects.all()

        paginated_cart = self.paginate_queryset(cart, request, self)
        cart_serializer = ShoppingSessionSerializer(paginated_cart, many=True)
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


class CartDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderView(APIView, PageNumberPagination):
    """
    1. Creates an Order
    2. Returns a list of 10 latest Order
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 Orders"
    )
    def get(self, request, format=None, *args, **kwargs):
        order = Order.objects.all()

        paginated_orders = self.paginate_queryset(order, request, self)
        order_serializer = ShoppingSessionSerializer(paginated_orders, many=True)
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


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
