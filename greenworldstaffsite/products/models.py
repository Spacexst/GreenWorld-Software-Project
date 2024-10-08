from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):

    name = models.TextField()
    description = models.TextField()
    price = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.description}. Price: ${self.price} '


class User(models.Model):

    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=55)
    department = models.CharField(max_length=255, choices=[('Management', 'Management'), (
        'Marketing', 'Marketing'), ('Customer Service', 'Customer Service')])
