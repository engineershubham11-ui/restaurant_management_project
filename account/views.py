from django.db import models

class contact(models.model):
    address = models.charfield(max_length=255)
    city = models.charfield(max_length=100)
    state = model.charfield(max_length=100)
    zip_code = models.charField(max_length=10)
    
    


    
    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"




