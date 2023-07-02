from django.contrib import admin

from apps.warehouse.models import WarehouseOrder


@admin.register(WarehouseOrder)
class WarehouseOrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "id", "status"]
    list_editable = ["status"]
    search_fields = ["id", "status"]
