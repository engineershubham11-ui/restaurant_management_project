from django.db import models

class contact(models.model):
    name = models.charfield(max_length=100)
    description = models.Textfield()
    price = models.DecimalField(max_digit=6, decimal_places=2)
    
    image = models.ImageField(upload_to='menu_image/', blank=True, null=True)


    
    def __str__(self):
        return self.name




