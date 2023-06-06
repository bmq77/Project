from django.db import models

# Create your models here.

class device(models.Model):
    laptopType = models.CharField(max_length=255)
    price = models.CharField(max_length= 255)
    description = models.CharField(max_length=100)


