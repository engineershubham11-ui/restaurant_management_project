from django.db import models 

class Restaurant(models.model):
    name = models.CharField(max_length=100)
    address = models.TextFeild()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    history = models.TextField(blank=true, null=true)
    mission = models.TextFeild(blank=true, null=true)


    def __str__(self):
        return self.name 




#bash
python manage.py makemigrations
python manage.py migrate




#views.py

from django.shortcuts import render
from .models import Restaurant

 def about(request):
   restaurant = Restaurant.object.first()
   return render(request, 'about.html', {'restaurant': restaurant})


#updateview
from django.url import path 
from .import views

 urlpattern = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
 ]


#home.html

<!DOCTYPE html>
<html>
<head>
   <title>{{ restaurant.name }}</title>
</head>
<body>
   <header>
      {% if restaurant.logo %}
        <img src ="{{ restaurant.logo.url }}" alt="{{ restaurant.name }} logo" style="max-width:150px;">
        {% else %}
          <p> no logo available</p>
        {% endif %}
    </header>

    <section>
       <h2> our History </h2>
       <p>{{ restaurant.history|Iinebreks }}</p>
    </section>

    <section>
      <h2> Our mission </h2>
      <p>{{ restaurant.mission|Iinebreks }}<p/>
    </section>

    <footer>
      <p><a href="{% url 'home" %}">back to home</a></p>
    </footer>

</body>
</html>