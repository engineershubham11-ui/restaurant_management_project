from django.db import models
from django.contrib.auth.models import user

class userprofile(models.model):
    user = models.oneToOneField(user, on_delete=model.CASCADE)

    name = models.charfield(max_length=100)
    phone_number = models.charfield(max_length=15)

    def __str__(self):
        return self.user.username



#model.py 

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=user)
def created_or_update_user_profile(sender,instance, created,**kwargs):
    if created:
        userprofile.object.create(user=instance, name=instance.get_full_name())
    else:
        instance.userprofile.save()











