# Generated by Django 3.2.6 on 2021-11-27 12:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210904_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cloudinaryimg',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]