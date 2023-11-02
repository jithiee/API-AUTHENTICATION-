from django.db import models

class Student(models.Model):
    name = models.CharField( max_length=50)
    roll = models.IntegerField()
    city = models.CharField( max_length=50)
    
    
    
# this signal create Auth token for users     

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
