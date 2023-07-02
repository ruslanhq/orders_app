from urllib.parse import urljoin

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.store.models import Order
from apps.store.serializers import OrderSerializer
from core.api_client import MakeRequest
from core.settings.base import WAREHOUSE_API_KEY, WAREHOUSE_URL


@receiver(post_save, sender=Order)
def sync_with_warehouse(created, instance, **kwargs):
    if created:
        url = urljoin(WAREHOUSE_URL, "/api/warehouse/order/create/")
        data = OrderSerializer(instance).data
        headers = {
            "X-API-Key": WAREHOUSE_API_KEY,
        }
        try:
            request = MakeRequest(  # noqa: F841
                uri=url, method="POST", data=data, headers=headers
            ).do_sync_request()
        except Exception as err:
            print(f"Error syncing with Warehouse: {err}")
