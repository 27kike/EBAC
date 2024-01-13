from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    color = models.TextField()
    seller = models.TextField()
    description = models.TextField()
    price = models.FloatField()