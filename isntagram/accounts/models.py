from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    introduction = models.TextField(blank=True)
    image_file = ProcessedImageField(
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 80},
        )