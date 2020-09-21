from rest_framework import serializers
from ..models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'address', 'phone', 'sent']
        