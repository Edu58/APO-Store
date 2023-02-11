from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductReview
from .serializers import ProductReviewSerializer


class ProductsReviewView(APIView, PageNumberPagination):
    """
    1. Creates a Product Review
    2. Returns a list of 10 latest Product Reviews
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 Product Reviews"
    )
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def get(self, request, format=None, *args, **kwargs):
        product_reviews = ProductReview.objects.all()

        paginated_product_reviews = self.paginate_queryset(product_reviews, request, view=self)
        product_reviews_serializer = ProductReviewSerializer(paginated_product_reviews, many=True)
        return Response(
            data=product_reviews_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=ProductReviewSerializer,
        operation_description="Creates a new Product Review"
    )
    def post(self, request, format=None, *args, **kwargs):
        product_reviews_serializer = ProductReviewSerializer(data=request.data)

        if product_reviews_serializer.is_valid():
            product_reviews_serializer.save()
            return Response(
                data=product_reviews_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=product_reviews_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProductReviewDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
