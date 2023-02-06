from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

from .models import Account, CustomerAddress, CustomerPayment


class AccountSerializer(ModelSerializer):
    """
    Converts the Account model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = Account
        fields = ("email", "password", "role")
        # Prevents the password hash from being returned
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        role = validated_data.get('role')
        account = Account.objects.create(**validated_data)

        admins_group, created = Group.objects.get_or_create(name="Admins")
        customers_group, created = Group.objects.get_or_create(name="Customers")

        if role is "Admin":
            account.groups.add(admins_group)
        else:
            account.groups.add(customers_group)

        return account


class CustomerAddressSerializer(ModelSerializer):
    """
    Converts the CustomerAddress model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = CustomerAddress
        fields = "__all__"


class CustomerPaymentSerializer(ModelSerializer):
    """
    Converts the CustomerPayment model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = CustomerPayment
        fields = "__all__"
