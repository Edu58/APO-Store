from rest_framework.serializers import ModelSerializer

from .models import ProductReview


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"
