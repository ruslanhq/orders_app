from urllib.parse import urljoin

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.warehouse.models import WarehouseOrder
from core.api_client import MakeRequest
from core.settings.base import STORE_API_KEY, STORE_URL


@receiver(post_save, sender=WarehouseOrder)
def sync_with_store(created, instance, **kwargs):
    if not created:
        url = urljoin(STORE_URL, "/api/store/order/update/")
        headers = {
            "X-API-Key": STORE_API_KEY,
        }
        data = {
            "id": instance.id,
            "order_number": instance.order_number,
            "status": instance.status,
        }
        try:
            request = MakeRequest(  # noqa: F841
                uri=url, method="PUT", data=data, headers=headers
            ).do_sync_request()
        except Exception as err:
            print(f"Error syncing with Store: {err}")
