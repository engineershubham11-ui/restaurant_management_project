from django.db import models

class contact(models.model):
    name = models.charfield(max_length=100)
    description = models.Textfield()
    price = models.DecimalField(max_digit=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_image/', blank=true, null=True)


    
    def __str__(self):
        return self.name


# views.py

from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    menu_items = menuItems.object.all()
    return render(request, 'menu.html', {'menu_items': menu_items})









