# Generated by Django 3.2.7 on 2021-10-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211015_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorm',
            name='hours',
            field=models.CharField(default='150', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseorm',
            name='code',
            field=models.CharField(blank=True, default='752DEA', max_length=6, verbose_name='Code'),
        ),
    ]
