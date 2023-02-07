from rest_framework.serializers import ModelSerializer

from .models import ShoppingSession


class ShoppingSessionSerializer(ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = "__all__"
