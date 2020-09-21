from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['meal']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ display Order model """
    list_display = ['id', 'name', 'address', 'phone', 'created',]
    list_filter = ['created', 'name']
    inlines = [OrderItemInline]

