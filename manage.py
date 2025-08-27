#views.py
from django.shortcuts import render
from datetime import datetime

def home(request);
  current_datetime = datetime.now()
  return render(request, 'home.html', {'current_datetime': current_datetime})



from django import template 

register = template.library()

@register.filter
def formate_datetime(value):
    return value.strftime("%d-%b-%y | %I:%M 0p%")