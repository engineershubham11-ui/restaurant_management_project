from django.db import models

class contactsubmission(models.model):
    name = models.charfield(max_length=100)
    email = models.Emailfield()
    submitted_at = models.dateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({ self.email})"


#form.py
from django import forms
froms .models import contactsubmission
class contactfrom(forms.modelform):
    class meta:
        model = contactsubmission
        fields = ['name','email']











