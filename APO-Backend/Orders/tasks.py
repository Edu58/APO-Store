import json

from django.contrib.auth import get_user_model
from celery import shared_task

from .serializers import OrderSerializer


@shared_task
def save_order(data):
    order_serializer = OrderSerializer(data=data)
    if order_serializer.is_valid():
        order_serializer.save()
