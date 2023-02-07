from django.db import models

# Create your models here.

class Item(models.Model):
    item_number = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    class meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
