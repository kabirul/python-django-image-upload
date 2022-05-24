from django.db import models

class Image(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

