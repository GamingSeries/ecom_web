# Generated by Django 4.1.6 on 2023-02-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0022_alter_merchant_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$4wsKsIgjwW39yRIe8StA0e$KDWgk+ET8z02+kIMvaNUbnh4iOnaB960AnuchIigHPE=', max_length=100),
        ),
    ]