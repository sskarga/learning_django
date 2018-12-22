from django.db import models

class Lan(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Address
    adr_id_city = models.IntegerField()
    adr_id_street = models.IntegerField()
    adr_id_home = models.IntegerField()

    #Config
    vlan = models.PositiveSmallIntegerField()
    network = models.GenericIPAddressField(protocol='IPv4')
    netmask = models.PositiveSmallIntegerField()
    gateway = models.GenericIPAddressField(protocol='IPv4')

# TYpe equipment. Example: Switch, Router or other
class Equipments_Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

# State equipment. Example: in line, not work, new or other
class Equipments_State(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Equipments_Model(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Link
    type = models.ForeignKey(Equipments_Type, on_delete=models.PROTECT)

    # Port ranges allocated to users
    userport_start = models.PositiveSmallIntegerField()
    userport_end = models.PositiveSmallIntegerField()

    note = models.CharField(max_length=200, blank=True)


class Equipments(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Link
    equipments_model = models.ForeignKey(Equipments_Model, on_delete=models.PROTECT)
    equipments_state = models.ForeignKey(Equipments_State, on_delete=models.DO_NOTHING)
    lan = models.ForeignKey(Lan, on_delete=models.DO_NOTHING)
    # Address
    adr_id_city = models.IntegerField()
    adr_id_street = models.IntegerField()
    adr_id_home = models.IntegerField()
    adr_entrance = models.SmallIntegerField()
    adr_floor = models.SmallIntegerField()

    # Hard config
    ip_address = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
    mac_adr = models.CharField(max_length=20, unique=True)
    serial = models.CharField(max_length=50, unique=True)

    # Other
    note = models.CharField(max_length=200, blank=True)

    create_at = models.DateTimeField(auto_created=True)


class Port_State(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Equipments_Port(models.Model):
    num_port = models.PositiveSmallIntegerField()
    ip_address = models.GenericIPAddressField(protocol='IPv4')

    # Link
    equipments_port = models.ForeignKey(Equipments, on_delete=models.PROTECT)
    port_state = models.ForeignKey(Port_State, on_delete=models.DO_NOTHING)
    lan = models.ForeignKey(Lan, on_delete=models.DO_NOTHING)


