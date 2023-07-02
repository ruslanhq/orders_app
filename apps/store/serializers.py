from rest_framework import serializers

from apps.store.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "order_number",
            "status",
        ]
