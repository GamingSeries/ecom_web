# Generated by Django 4.1.6 on 2023-02-11 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20230211_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller_register',
            name='password',
        ),
    ]