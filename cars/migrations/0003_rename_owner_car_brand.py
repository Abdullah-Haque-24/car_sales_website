# Generated by Django 5.0.7 on 2024-08-24 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_brand_car_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='owner',
            new_name='brand',
        ),
    ]