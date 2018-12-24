# Generated by Django 2.1.4 on 2018-12-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0004_auto_20181224_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipments',
            name='lan',
        ),
        migrations.AlterField(
            model_name='equipments',
            name='adr_entrance',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='adr_floor',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='create_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]