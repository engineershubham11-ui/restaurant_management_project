from django.db import models 

class Restaurant(models.model):
    name = models.CharField(max_length=100)
    address = models.TextFeild()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)


    def __str__(self):
        return self.name 




#bash
python manage.py makemigrations
python manage.py migrate


#setting.pr
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'


#views.py

from django.conf import setting
from django.conf.url.static import static 

 urlpattern = [
    #...
 ]

if setting.DEBUG:
    urlpattern += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)




#updateview
from django.shotcuts import render
from .models import Restaurant 

 def home(request):
    restaurant = Restaurant.object.first()
    return render(request, 'home.html', {'restaurant' : restaurant})



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

    <h1> welcome to {{ restaurant.name }}</h1>
    <p>Address: {{ restaurant.address }}</p>
    <p> Phone: <a href="tel: {{restaurant.phone_number }}">{{ restaurant.phone_number }}</a></p>
    
</body>
</html>