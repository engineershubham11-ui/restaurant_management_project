from django.http import HttpResponse
from .models import restaurant 

def home(request):
    restaurant = restaurant.object.first()
    name = restaurant.name if restaurant else "our Restaurant "
    return HttpResponse(f"<h1>welcome to {name}</h1>")




#setting.py

RESTAURANT_NAME = "Food Paradise"

#urls.py

from django.urls import path
from .view import home

urlpattern = [
    path('',home, name='home'),
]