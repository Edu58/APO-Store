from rest_framework.serializers import ModelSerializer

from .models import ProductCategory, Discount


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"
