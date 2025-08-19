from django.shortcuts import render
from .model import MenuItems

def home(request):
    context = {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "My Restaurant"),
        "restaurant_address": getar(setting, "RESTAURANT_ADDRESS","123 Main street, city, country"),
        "map_embed_url": "https://www.google.com/maps/embed/v1/places?key=YOUR_API_KEY&q=123+main+street+city+country"

    }
    return render(request,"home.html", context)



#home.html
<!DOCTYPE html> 
<html>
<head>
   <title> {{ restaurant_name }}</title>
</head>
<body>
  <h1> welcome to {{restaurant_name }}</h1>

<h2>find us</h2>
<p>{{ restaurant_address }}</p>

<iframe
width="600"
height="450"
style="border:0"
loading="lazy"
allowfullscreen
referrerpolicy="no-referrer-when-downgrade"
src="{{map_embed_url }}">
</iframe>
</body>
</html>