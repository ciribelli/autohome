# Generated by Django 3.0.4 on 2020-04-25 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('controleambiente', '0005_auto_20200425_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='arcondstate',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
