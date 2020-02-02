from django.db import models
import datetime as dt

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'images/', default="")
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
   
class Category(models.Model):
    category = models.CharField(max_length =30)