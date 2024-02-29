from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    content = models.TextField()
    category = models.ImageField(upload_to = 'photos')
    tags = models.ArrayField(models.CharField(max_length = 30))
    