from django.urls import path

from apps.warehouse.views import WarehouseOrderView

urlpatterns = [
    path("order/create/", WarehouseOrderView.as_view(), name="warehouse_order_create"),
    path("order/update/", WarehouseOrderView.as_view(), name="warehouse_order_update"),
]
