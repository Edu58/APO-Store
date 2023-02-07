from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShoppingSession
from .serializers import ShoppingSessionSerializer


# Create your views here.
class ShoppingSessionView(APIView):
    """
    1. Creates a Shpping Session
    2. Returns a list of 10 latest Shopping Sessions
    """

    @swagger_auto_schema(
        operation_description="Returns a list of the latest 10 shopping sessions"
    )
    def get(self, format=None, *args, **kwargs):
        shopping_session = ShoppingSession.objects.all()[:10]
        shopping_session_serializer = ShoppingSessionSerializer(shopping_session, many=True)
        return Response(
            data=shopping_session_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=ShoppingSessionSerializer,
        operation_description="Creates a new Shopping Session"
    )
    def post(self, request, format=None, *args, **kwargs):
        shopping_session_serializer = ShoppingSessionSerializer(data=request.data)

        if shopping_session_serializer.is_valid():
            shopping_session_serializer.save()
            return Response(
                data=shopping_session_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=shopping_session_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
