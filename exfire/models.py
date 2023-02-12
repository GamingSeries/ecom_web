from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200 , default='')
    address = models.CharField(max_length=200   , default='')
    phone_number = models.CharField(max_length=200  , default='')
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name