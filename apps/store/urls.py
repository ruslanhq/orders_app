from django.urls import path

from apps.store.views import OrderView

urlpatterns = [
    path("order/update/", OrderView.as_view(), name="store_order_update"),
]
