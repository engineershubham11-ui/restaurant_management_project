session ['cart'] = {
    'item_id': quantity,
    'item_id_2': quantity,
}

#utils.py

def get_cart_count(session):
    cart = session.get('cart',{})
    return sum(cart.value())


#views.py

from django.shortcuts import render
from .models import Restaurant
from .utils import get_cart_count

def home(request):
    restaurant = restaurant.object.first()
    cart_count = get_cart_count(request.session)
    return render(request, 'home.html',){
        'restaurant': restaurant, 
        'cart_court': cart_count
    })