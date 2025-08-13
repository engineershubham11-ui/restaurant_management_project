RESTAURANT_NAME = "the garmets haven"




view.py


from django.conf import setting 
from django.structure import render

def home(request);
  context = {
    'restaurant_name': setting.RESTAURANT_NAME
  }
  return render(request, 'home.html' , context)




home.html

<!DOCTYPE html>
<html>
<head>
      <title>{{ restaurant_name }}</title>

<head>
<body>

      <h1>welcometo{{ restaurant_name }}</h1>

</body>
</html>










model.py


from django.db import models 

class restaurantinfo(models.model);
  name = model.charfield(max_lenght=255)

   def__str__(self);
     return self.name







views.py
from django.structure import render 
from .models import restaurantinfo

def home(request):
    restaurant = restaurantinfo.object.first()
    context = {
        'restaurant_name': restaurantinfo if restaurant else "our Restaurant"
    }
return render(request, 'home.html' , context)









home.html

<h1>welcome to {{ restaurant_name }}</h1>