# Generated by Django 3.2 on 2022-12-12 13:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255, verbose_name='image'),
        ),
    ]
