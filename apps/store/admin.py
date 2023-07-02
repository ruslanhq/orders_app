from django.contrib import admin

from apps.store.models import Order


@admin.register(Order)
class StoreOrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "id", "status"]
    list_editable = ["status"]
    search_fields = ["id", "status"]
