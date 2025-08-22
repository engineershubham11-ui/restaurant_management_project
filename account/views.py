
from django.db import models

class menuinfo(models.model):
    name = models.charField(max_length=100)
    description = models.textfield()
    prices = models.decimalfield(max_length=6, decimal_places=2)
    image  = model.imagefield(upload_to='menu_images/', blank=true, null=true)

   
    
    def __str__(self):
        return self.name



setting.py

import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')