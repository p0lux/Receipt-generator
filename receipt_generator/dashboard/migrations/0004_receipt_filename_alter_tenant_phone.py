# Generated by Django 4.0 on 2021-12-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_home_tenant_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='filename',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='phone',
            field=models.IntegerField(verbose_name=10),
        ),
    ]
