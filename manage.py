from django.shortcuts import render
from django.urls import reverse

def home(request):
    breadcrumbs = [("home",None)]
    return render(request,"home.html", {"breadcrumbs": breadcrumbs})

def menu(request):
    breadcrumbs = [
        ("Home", reverse("home")),
        ("Menu", None),
    ]
    return render(request, "menu.html", {"breadcrumbs": breadcrumbs})

def order_confirmation(request):
    breadcrumbs = [
        ("Home", reverse("home")),
        ("Menu", reverse("menu")),
        ("Order configration", None),
    ]
    return render(request, "order_configration.html",{"breadcrumbs": breadcrumbs})

#home.html

{% extend "base.html" %}

{% block content %}
{% include "partials/breadcrumbs.html" %}


<div class="container mt-3">
<!--content-->

</div>
{% endblock %}