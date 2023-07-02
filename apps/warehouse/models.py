from django.db import models

from apps.store.models import BaseModel


class WarehouseOrder(BaseModel):
    STATUS_ORDER_CHOICES = (
        ("new", "New"),
        ("in_process", "In Process"),
        ("stored", "Stored"),
        ("send", "Send"),
    )

    order_number = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=STATUS_ORDER_CHOICES, default="new"
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        app_label = "warehouse"

    def __str__(self):
        return self.order_number
