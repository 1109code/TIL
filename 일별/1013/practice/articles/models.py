from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)