from rest_framework.serializers import ModelSerializer

from .models import Customer


class CustomerSerializer(ModelSerializer):
    """
    Converts the Customer model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = Customer
        fields = ("email", "password",)
