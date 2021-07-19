from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/')