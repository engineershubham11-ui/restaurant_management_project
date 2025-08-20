import request 
from django.shortcuts import render 

def homepage (request):

    response = request.get("http://127.0.0.1:8000/api/menu/")
    menu_items = response.json() if response.status_code == 200 else []

    return render(request, "homepage.html", {"menu_items": menu_items})












