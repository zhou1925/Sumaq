from django.db import models
from meals.models import Meal


class Order(models.Model):
    """ Order Model """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    class Meta:
        ordering = ('-created',)

    def get_total_cost(self):
        """ return total cost of an order """
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """ Order detail of OrderModel """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        """ return cost of an item """
        return self.price * self.quantity
