# Generated by Django 2.1.4 on 2018-12-26 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_auto_20181225_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog_lan',
            name='location',
        ),
    ]
