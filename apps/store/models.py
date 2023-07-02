from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(BaseModel):
    STATUS_ORDER_CHOICES = (
        ('new', 'New'),
        ('in_process', 'In Process'),
        ('stored', 'Stored'),
        ('send', 'Send'),
    )

    order_number = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=STATUS_ORDER_CHOICES,
        default='new'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        app_label = 'store'

    def __str__(self):
        return self.order_number
