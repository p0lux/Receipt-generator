# Generated by Django 4.0 on 2021-12-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sudo',
            field=models.BooleanField(default=False),
        ),
    ]
