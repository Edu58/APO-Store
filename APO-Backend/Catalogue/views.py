from django.views.decorators.vary import vary_on_cookie
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import ProductCategory, Discount, Product
from .serializers import ProductCategorySerializer, DiscountSerializer, ProductSerializer


# Create your views here.
class ProductCategoryView(APIView, PageNumberPagination):
    """
    1. Creates a Product Category
    2. Returns a list of 10 latest Product Categories
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 product categories"
    )
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 5))
    def get(self, request, format=None, *args, **kwargs):
        product_categories = ProductCategory.objects.all()
        paginated_categories = self.paginate_queryset(product_categories, request, view=self)
        product_categories_serializer = ProductCategorySerializer(paginated_categories, many=True)
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


class ProductCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class DiscountView(APIView, PageNumberPagination):
    """
    1. Creates a Discount
    2. Returns a list of 10 latest Discounts
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 discounts"
    )
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 5))
    def get(self, request, format=None, *args, **kwargs):
        discounts = Discount.objects.all()

        paginated_discounts = self.paginate_queryset(discounts, request, self)
        discounts_serializer = ProductCategorySerializer(paginated_discounts, many=True)
        return Response(
            data=discounts_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=DiscountSerializer,
        operation_description="Creates a new Discount"
    )
    def post(self, request, format=None, *args, **kwargs):
        discounts_serializer = DiscountSerializer(data=request.data)

        if discounts_serializer.is_valid():
            discounts_serializer.save()
            return Response(
                data=discounts_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=discounts_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DiscountDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class ProductView(APIView, PageNumberPagination):
    """
    1. Creates a Product
    2. Returns a list of 10 latest Products
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 products"
    )
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 5))
    def get(self, request, format=None, *args, **kwargs):
        products = Product.objects.all()

        paginated_products = self.paginate_queryset(products, request, self)
        products_serializer = ProductSerializer(paginated_products, many=True)
        return Response(
            data=products_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=ProductSerializer,
        operation_description="Creates a new Product"
    )
    def post(self, request, format=None, *args, **kwargs):
        products_serializer = ProductSerializer(data=request.data)

        if products_serializer.is_valid():
            products_serializer.save()
            return Response(
                data=products_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=products_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
