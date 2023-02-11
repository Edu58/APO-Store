from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Account, CustomerAddress, CustomerPayment, Profile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customizes token claims by added extra fields
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # custom claims
        token['email'] = user.email
        token['role'] = user.role

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AccountSerializer(ModelSerializer):
    """
    Converts the Account model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = Account
        fields = ("id", "email", "password", "role")
        # Prevents the password hash from being returned
        extra_kwargs = {
            "id": {
                "read_only": True
            },
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        role = validated_data.get('role')
        account = Account.objects.create(**validated_data)
        account.set_password(validated_data.get('password'))

        admins_group, created = Group.objects.get_or_create(name="Admins")
        customers_group, created = Group.objects.get_or_create(name="Customers")

        if role is "Admin":
            account.groups.add(admins_group)
            account.save()
        else:
            account.groups.add(customers_group)
            account.save()

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


class ProfileSerializer(ModelSerializer):
    """
    Converts the Profile model data to JSON which can be passed on and understood by other systems
    """

    class Meta:
        model = Profile
        fields = "__all__"
