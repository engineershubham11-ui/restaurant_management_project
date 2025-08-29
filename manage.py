from django.shortcuts import render
import random

def order_confirmation(request):
    order_number = random.randint(1000, 9999)
    breadcrumbs = [
        ("Home", "/"),
        ("Order configration", None),
    ]
    return render(request, "order_configration.html",{
    "order_number": order_number,
    "breadcrumbs": breadcrumbs
    })

#home.html

{% extend "base.html" %}


{% block content %}
<div class="container mt-5 text-center">
<h2>order configration</h2>
<p> Thank you! your order has been placed sucessfully.</p>


{% if order_number %}
<p><strong>Order Number:</strong> {{ order_number }}</p>
{% endif %}

<a href="{% url 'home" %}" class="btn btn-primary mt-3"> Return to Home</a>

</div>
{% endblock %}

