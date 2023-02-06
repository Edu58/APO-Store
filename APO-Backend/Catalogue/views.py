from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductCategory
from .serializers import ProductCategorySerializer


# Create your views here.
class ProductCategoryView(APIView):
    """
    1. Creates a Product Category
    2. Returns a list of 10 latest Product Categories
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 product categories"
    )
    def get(self, format=None, *args, **kwargs):
        product_categories = ProductCategory.objects.all()[:10]
        product_categories_serializer = ProductCategorySerializer(product_categories, many=True)
        return Response(
            data=product_categories_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=ProductCategorySerializer,
        operation_description="Creates a new Product Category"
    )
    def post(self, request, format=None, *args, **kwargs):
        product_category_serializer = ProductCategorySerializer(data=request.data)

        if product_category_serializer.is_valid():
            product_category_serializer.save()
            return Response(
                data=product_category_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=product_category_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )