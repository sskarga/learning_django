# Generated by Django 2.1.4 on 2019-01-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='estate',
            field=models.CharField(choices=[('WN', 'Склад (новое)'), ('WU', 'Склад (б/у)'), ('WB', 'Склад (сломано)'), ('I', 'Установлено'), ('UR', 'В ремонте'), ('WO', 'Списано')], default='WN', max_length=2),
        ),
        migrations.DeleteModel(
            name='EState',
        ),
    ]