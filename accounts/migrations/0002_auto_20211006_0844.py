# Generated by Django 3.2.7 on 2021-10-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(blank=True, default='S423825', max_length=7, verbose_name='Student code'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='code',
            field=models.CharField(blank=True, default='TC073C0', max_length=7, verbose_name='Teacher code'),
        ),
    ]
