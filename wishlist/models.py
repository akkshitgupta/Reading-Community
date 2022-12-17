from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    genre = models.CharField(max_length=25)