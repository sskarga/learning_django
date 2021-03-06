# Generated by Django 2.1.4 on 2018-12-25 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('userport_start', models.PositiveSmallIntegerField()),
                ('userport_end', models.PositiveSmallIntegerField()),
                ('note', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('adr_entrance', models.SmallIntegerField(blank=True, null=True)),
                ('adr_floor', models.SmallIntegerField(blank=True, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('mac', models.CharField(max_length=20, unique=True)),
                ('serial', models.CharField(max_length=50, unique=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('emodel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipments.EModel')),
            ],
        ),
        migrations.CreateModel(
            name='EState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vlan', models.PositiveSmallIntegerField()),
                ('network', models.GenericIPAddressField(protocol='IPv4')),
                ('netmask', models.PositiveSmallIntegerField(default=24)),
                ('gateway', models.GenericIPAddressField(protocol='IPv4')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_number', models.PositiveSmallIntegerField()),
                ('ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('enabled', models.BooleanField(default=True)),
                ('equipments', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipments.Equipments')),
            ],
        ),
        migrations.AddField(
            model_name='equipments',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='equipments.EState'),
        ),
        migrations.AddField(
            model_name='equipments',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location.Address'),
        ),
        migrations.AddField(
            model_name='emodel',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipments.EType'),
        ),
    ]
