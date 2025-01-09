from django.db import models

class Photo(models.Model):
    image_path = models.CharField(max_length=255)
    description = models.TextField()
    hashtags = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
