from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Catalogue.models import Product
from Catalogue.serializers import ProductSerializer


# Create your views here.
class QueryProducts(APIView):
    """
    Performs a Full-Text search for products based on their descriptions and names.
    """

    @swagger_auto_schema(
        operation_description="Returns a list of product names with the query parameter passed"
    )
    def get(self, request, format=None, *args, **kwargs):
        query_param = request.query_params.get('product_name', None)
        products = Product.objects.filter(
            name__icontains=f'{query_param}'
        ).values_list('id', 'name', 'size', 'price', 'discount')

        results_serializer = ProductSerializer(products, many=True)

        data = {
            "count": len(results_serializer.data),
            "results": results_serializer.data
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
