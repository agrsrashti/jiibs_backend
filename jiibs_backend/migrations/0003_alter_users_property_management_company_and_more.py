# Generated by Django 5.0 on 2023-12-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiibs_backend', '0002_media_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='property_management_company',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='property_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
