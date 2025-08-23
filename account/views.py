from django.db import models 

class Restaurant(models.model):
    name = models.CharField(max_length=100)
    address = models.TextFeild()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name 




#bash
python manage.py makemigrations
python manage.py migrate



#views.py

from django.shortcuts import render 
from .models import Restaurant 

 def home(request):
    restaurant = Restaurant.object.first()
    return render(request, 'home.html', {'restaurant': restaurant})


<!DOCTYPE html>
<html>
<head>
   <title>{{ restaurant.name }}</title>
</head>
<body>
    <h1> welcome to {{ restaurant.name }}</h1>
    <p>Address: {{ restaurant.address }}</p>
    <p>Phone: <a href="tel:{{ restaurant.phone_number }}">{{ restaurant.phone_number}}</a></p>
</body>
</html>