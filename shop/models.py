from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    image_path = models.CharField(max_length=255)
    description = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'shop_photo'
