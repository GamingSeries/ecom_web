# Generated by Django 4.1.6 on 2023-02-11 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_rename_seller_register_seller'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Seller', 'verbose_name_plural': 'Sellers'},
        ),
    ]