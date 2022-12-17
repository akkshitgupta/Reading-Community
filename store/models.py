from django.db import models

# Create your models here.

class Members(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    eMail = models.CharField(max_length=14)
    passWord = models.CharField(max_length=14)

class Wishlist(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    genre = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)