# Generated by Django 3.2.7 on 2021-10-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorm',
            name='code',
            field=models.CharField(blank=True, default='2B4C70', max_length=6, verbose_name='Code'),
        ),
    ]
