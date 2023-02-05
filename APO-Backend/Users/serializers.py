from rest_framework.serializers import ModelSerializer

from .models import Customer, CustomerAddress


class CustomerSerializer(ModelSerializer):
    """
    Converts the Customer model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = Customer
        fields = ("email", "password",)
        # Prevents the password hash from being returned
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


class CustomerAddressSerializer(ModelSerializer):
    """
    Converts the CustomerAddress model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = CustomerAddress
        fields = "__all__"
