# Generated by Django 4.1.6 on 2023-02-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0018_alter_merchant_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$Eq9XW6HWKkdcbBBFy9Wvhb$OsasontBIgfU1T5ddVeHpjT9UjJ4+iLBozLvxS3LEa4=', max_length=100),
        ),
    ]