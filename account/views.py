from django.db import models

class contact(models.model):
    name = models.charfield(max_length=100)
    email = models.emailfield()

    submittted_at = Models.dateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, ({self.email})"









