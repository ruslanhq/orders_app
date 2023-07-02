from urllib.parse import urljoin

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.warehouse.models import WarehouseOrder
from core.api_client import MakeRequest
from core.settings.base import STORE_URL


@receiver(post_save, sender=WarehouseOrder)
def sync_with_store(created, instance, **kwargs):
    if not created:
        url = urljoin(STORE_URL, "/api/store/order/update/")
        data = {
            "id": instance.id,
            "order_number": instance.order_number,
            "status": instance.status,
        }
        try:
            request = MakeRequest(  # noqa: F841
                uri=url, method="PUT", data=data
            ).do_sync_request()
        except Exception as err:
            print(f"Error syncing with Store: {err}")
