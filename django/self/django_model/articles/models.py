from django.db import models

# 1.모델 클라스 생성 
#    models.Model 상속
class Article(models.Model):
    # title -> char
    title = models.CharField(max_length=10)
    # content -> text
    content = models.TextField()
    # created_at -> Datetime
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at -> Datetime
    updated_at = models.DateTimeField(auto_now=True)
