# Generated by Django 4.0 on 2021-12-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_home_informations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='surface',
            field=models.IntegerField(),
        ),
    ]
