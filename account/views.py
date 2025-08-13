from django.shortcuts import render

def menu_items(request):
    menu = [


{"name": "margherita pizza","price":8.99, "description": "classic pizza with mozzarella and basil"},
{"name": "spaghetti carbonara", "price" : 10.50, "description": "pasta with pancetta,egg, and parmesan"},
{"name": "caser salad", "price":6.75, "description" "romaine lettuce with caser dressing"},


]
return render(request,"menu.html", {"menu_items": menu})



menu.html
<!DOCTYPE html>
<html>
<head>
     <title>menu</title>
</head>
<body>
    <h1> Our menu </h1>
    <ul>
        {% for item in menu_items %}
           <li>
              <strong>{{ item.name }}</strong> -${{ item.price }} <br>
              <em> {{ item.description }}</em>
            </li>
        {% endfor %}
    </ul>
</body>
</html>










url.py

from django.urls import path 
from . import views

urlpattern = [
    path('menu/', views.menu_items, name='menu_items'),
]

