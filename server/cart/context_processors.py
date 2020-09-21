from .cart import Cart

def cart(request):
    """ context processor for shopping cart """
    return {'cart': Cart(request)}