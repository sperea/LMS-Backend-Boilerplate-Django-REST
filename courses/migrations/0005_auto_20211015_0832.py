# Generated by Django 3.2.7 on 2021-10-15 08:32

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20211013_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorm',
            name='code',
            field=models.CharField(blank=True, default='D3AA43', max_length=6, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='courseorm',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
