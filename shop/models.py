from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=255)
    
class Photo(models.Model):
    image_path = models.CharField(max_length=255)
    description = models.TextField()
    hashtags = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'shop_photo'

    def get_hashtags_list(self):
        """Возвращает список хэштегов"""
        return [tag.strip() for tag in self.hashtags.split(",")]