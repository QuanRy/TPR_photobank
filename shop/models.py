from django.db import models

class ProductType(models.Model):     
    name = models.CharField(max_length=200) 


# Create your models here. (first commit)
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    type = models.ForeignKey('ProductType', on_delete=models.CASCADE)


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)