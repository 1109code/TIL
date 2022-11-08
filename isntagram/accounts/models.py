from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    introduction = models.CharField(blank=True)
    image_file = models.ImageField(upload_to='', height_field='300', width_field='300', quality=90, format='JPEG')