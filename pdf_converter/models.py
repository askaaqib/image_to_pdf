from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(blank=True)