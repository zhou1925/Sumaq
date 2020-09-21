from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from meals.models import Meal
from .forms import CartAddMealForm
from .cart import Cart


@require_POST
def cart_add(request, meal_id):
    """ add item to shopping cart """
    cart = Cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    form = CartAddMealForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(meal=meal,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('meals:meal_list')


@require_POST
def cart_remove(request, meal_id):
    """ user can remove items from his shopping cart """
    cart = Cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    cart.remove(meal)
    return redirect('meals:meal_list')


def cart_detail(request):
    """ return shopping cart detail """
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
