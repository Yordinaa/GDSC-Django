from django.db import models
from BlogApp.models import Post 

class Comment(models.Model):
  content = models.TextField()
  author = models.CharField(max_length=100)
  date = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
# Create your models here.
