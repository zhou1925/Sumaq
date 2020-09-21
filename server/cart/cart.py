from decimal import Decimal
from django.conf import settings
from meals.models import Meal


class Cart:
    """ Cart Model for manage shopping cart """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, meal, quantity=0, override_quantity=False):
        """ Add meal to cart """
        meal_id = str(meal.id)
        if meal_id not in self.cart:
            self.cart[meal_id] = {'quantity': 0, 'price': str(meal.price)}
        if override_quantity:
            self.cart[meal_id]['quantity'] = quantity
        else:
            self.cart[meal_id]['quantity'] += quantity
        self.save()

    def save(self):
        """ change session state """
        self.session.modified = True

    def remove(self, meal):
        """ remove an item of the cart """
        meal_id = str(meal.id)
        if meal_id in self.cart:
            del self.cart[meal_id]
            self.save()

    def __iter__(self):
        meal_ids = self.cart.keys()
        meals = Meal.objects.filter(id__in=meal_ids)

        cart = self.cart.copy()
        for meal in meals:
            cart[str(meal.id)]['meal'] = meal

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """ return total sum of shopping cart """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """ delete session cart """
        del self.session[settings.CART_SESSION_ID]
        self.save()