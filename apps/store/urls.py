from django.urls import path

from apps.store.views import OrderView

urlpatterns = [
    path("store_order/update/", OrderView.as_view(), name="store_order_update"),
]
