# Generated by Django 3.2.6 on 2022-09-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_devicecategory_electroniccomponent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electroniccomponent',
            name='deviceCategories',
            field=models.ManyToManyField(to='blog.DeviceCategory'),
        ),
    ]
