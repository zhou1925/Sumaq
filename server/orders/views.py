from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    """ the user can create order and 
    the cart object manage the order """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        meal=item['meal'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return render(request,
                        'orders/order_created.html',
                        {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                        'orders/order.html',
                        {'cart': cart, 'form': form})
