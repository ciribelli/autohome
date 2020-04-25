# Generated by Django 3.0.4 on 2020-04-25 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controleambiente', '0003_remove_ambiente_arcond'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArcondState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onoff', models.BooleanField(default=False)),
                ('local', models.ForeignKey(default=1, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='controleambiente.Local')),
            ],
        ),
    ]
