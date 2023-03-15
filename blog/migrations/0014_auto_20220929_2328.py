# Generated by Django 3.2.6 on 2022-09-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_electroniccomponent_devicetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='electroniccomponent',
            name='workingCurrent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electroniccomponent',
            name='workingVoltage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='electronic_components',
            field=models.ManyToManyField(to='blog.ElectronicComponent'),
        ),
    ]
