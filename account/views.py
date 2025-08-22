
from django.db import models

class restaurantinfo(models.model):
    name = models.charField(max_length=100)
    address = models.charfield()
    city = models.charfield(max_length=50)
    state = model.charfield(max_length=50)
    zip_code = models.charField(max_length=10)
    opening_hours = models.JSONField(default=dict)
    


    
    def __str__(self):
        return self.name