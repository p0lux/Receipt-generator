# Generated by Django 4.0 on 2021-12-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_receipt_filename_alter_tenant_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='informations',
            field=models.TextField(default=''),
        ),
    ]