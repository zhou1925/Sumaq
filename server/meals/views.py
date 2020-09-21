from django.shortcuts import render
from cart.forms import CartAddMealForm
from .models import Meal


def meal_list(request):
    """ Return Meal list and cart form """
    meals = Meal.objects.all()
    cart_form = CartAddMealForm()
    return render(request, 'meals/meals.html', {'meals': meals, 'cart_form': cart_form})
