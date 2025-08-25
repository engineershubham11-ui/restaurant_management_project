from django.db import models

class RestaurantInfo(models.model):
    name = models.charfield(max_length=100)
    email = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)



    def __str__(Self):
        return self.name



from django.contrib import admin
from .models import RestaurantInfo


admin.site.register(RestaurantInfo)




#view.py

from django.shortcuts import render
from .models import RestaurantInfo

def homepage(request):
   restaurant = RestaurantInfo.object.first()
   return render(request, 'homepage.html',{'restaurant': restaurant})



<div style="text-align: center; margin-top: 10px">
  <p style="font-size: 1.2rem; font-weight: bold; colour: #333;">
  call us:<a href = "tel:{{ restaurant.phone }}" style="colour: #007BFF;">{{ restaurant.phone }}</a>
  </p>
</div>