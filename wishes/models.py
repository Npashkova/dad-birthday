from django.db import models

# Create your models here.


class Wish(models.Model):
    wish_video = models.FileField(upload_to='videos/')
    video_caption = models.CharField(max_length=300)