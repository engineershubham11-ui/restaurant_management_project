#views.py
from django.shortcuts import render

def privacy_policy(request):
    return render(request, "privacy_policy.html")

#urls.py
from django.urls import path
from . import views

urlpattern = [
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    
]