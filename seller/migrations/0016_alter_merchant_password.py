# Generated by Django 4.1.6 on 2023-02-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0015_alter_merchant_options_alter_merchant_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$x38RllHE7qkj2qXjWMpZUG$CkETqF6YNfIu87Xk5z5yglZH+XkwXDaMPeCRMJwQIfc=', max_length=100),
        ),
    ]
