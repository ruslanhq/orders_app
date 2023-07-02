from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.store.models import Order
from apps.store.serializers import OrderSerializer
from core.authentication import AuthToken


class OrderView(APIView):
    authentication_classes = [AuthToken]

    def put(self, request, *args, **kwargs):
        if "id" not in request.data:
            return Response(
                {"error": "id is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        instance = get_object_or_404(Order, id=request.data["id"])

        serializer = OrderSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
