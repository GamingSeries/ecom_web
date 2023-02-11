from django.db import models

# Create your models here.

class Seller_Register(models.Model):
    seller_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Seller_Register'
        verbose_name_plural = 'Seller_Registers'

    def __str__(self):
        return self.name

class Item(models.Model):
    item_number = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name