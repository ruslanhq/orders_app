from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouse.models import WarehouseOrder
from apps.warehouse.serializers import WarehouseOrderSerializer
from core.authentication import AuthToken


class WarehouseOrderView(APIView):
    authentication_classes = [AuthToken]

    def post(self, request, *args, **kwargs):
        serializer = WarehouseOrderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if "id" not in request.data:
            return Response(
                {"error": "id is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        instance = get_object_or_404(WarehouseOrder, id=request.data["id"])

        serializer = WarehouseOrderSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
