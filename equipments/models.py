from django.db import models
from location.models import Address

class Lan(models.Model):
    name = models.CharField(max_length=50)

    #Config
    vlan = models.PositiveSmallIntegerField()
    network = models.GenericIPAddressField(protocol='IPv4')
    netmask = models.PositiveSmallIntegerField(default=24)
    gateway = models.GenericIPAddressField(protocol='IPv4')

    def __str__(self):
        return self.name

# TYpe equipment. Example: Switch, Router or other
class EType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# State equipment. Example: in line, not work, new or other
class EState(models.Model):
    WAREHOUSE_NEW = 'WN'
    WAREHOUSE_USED = 'WU'
    WAREHOUSE_BROKEN = 'WB'
    INSTALLED = 'I'
    UNDER_REPAIT = 'UR'
    WRITEN_OFF = 'WO'

    STATE_CHOICES = (
        (WAREHOUSE_NEW, 'Склад (новое)' ),
        (WAREHOUSE_USED, 'Склад (б/у)' ),
        (WAREHOUSE_BROKEN, 'Склад (сломано)' ),
        (INSTALLED, 'Установлено' ),
        (UNDER_REPAIT, 'В ремонте' ),
        (WRITEN_OFF, 'Списано' ),
    )

    name = models.CharField(
            max_length=2, 
            choices = STATE_CHOICES,
            default = WAREHOUSE_NEW,
        )


class EModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Link
    type = models.ForeignKey(EType, on_delete=models.PROTECT)

    # Port ranges allocated to users
    userport_start = models.PositiveSmallIntegerField()
    userport_end = models.PositiveSmallIntegerField()

    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Equipments(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Link
    emodel = models.ForeignKey(EModel, on_delete=models.PROTECT)
    estate = models.ForeignKey(EState, on_delete=models.DO_NOTHING)
    
    # Address
    location = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    adr_entrance = models.SmallIntegerField(blank=True, null=True)
    adr_floor = models.SmallIntegerField(blank=True, null=True)

    # Hard config
    ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
    mac = models.CharField(max_length=20, unique=True)
    serial = models.CharField(max_length=50, unique=True)

    # Other
    note = models.CharField(max_length=200, blank=True, null=True,)

    create_at = models.DateTimeField(blank=True, null=True, auto_created=True)

    def __str__(self):
        return self.name


class Catalog_Lan(models.Model):
    # Link
    lan = models.ForeignKey(Lan, on_delete=models.DO_NOTHING)
    equipments = models.ForeignKey(Equipments, on_delete=models.DO_NOTHING)


class Port(models.Model):
    port_number = models.PositiveSmallIntegerField()
    ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    # Link
    equipments = models.ForeignKey(Equipments, on_delete=models.PROTECT)
    lan = models.ForeignKey(Lan, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "port {0}".format(self.port_number)


