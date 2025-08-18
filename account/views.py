from django.shortcuts import render
from .model import MenuItems

def menu_page(request):
    items = MenuItems.objects.all()
    return render(request, 'menu.html', {'items': items})
    