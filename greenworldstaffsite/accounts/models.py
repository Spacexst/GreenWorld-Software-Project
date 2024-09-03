from django.db import models

# Create your models here.
class Staff(models.Model):

    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.full_name