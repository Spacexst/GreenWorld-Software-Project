from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products',
                              default='default_image.jpg')
    price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}: {self.description}. Price: ${self.price} '


class NewProduct(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products',
                              default='default_image.jpg')
    price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}: {self.description}. Price: ${self.price} '



