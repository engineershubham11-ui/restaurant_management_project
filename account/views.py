from django.db import models 

class menuItem(models.model):
    name = models.charField(max_length=200)
    description = models.TextField(blank=true, null=true)
    price = models.decimalField(max_digit=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    