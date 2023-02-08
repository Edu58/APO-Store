from rest_framework.serializers import ModelSerializer

from .models import PaymentDetails


class PaymentDetailsSerializer(ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = "__all__"
