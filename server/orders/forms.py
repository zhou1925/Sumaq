from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """ OrderForm for create and Order """
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone']



