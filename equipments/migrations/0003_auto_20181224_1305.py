# Generated by Django 2.1.4 on 2018-12-24 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_auto_20181224_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lan',
            old_name='adr_id_home',
            new_name='location',
        ),
    ]