from rest_framework import serializers

from apps.warehouse.models import WarehouseOrder


class WarehouseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = [
            "order_number",
            "status",
        ]
