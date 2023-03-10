from rest_framework.serializers import ModelSerializer

from .models import ShoppingSession, Cart, Order


class ShoppingSessionSerializer(ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
