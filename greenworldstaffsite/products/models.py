from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f'{self.name}: {self.description}. Price: ${self.price} '
    

