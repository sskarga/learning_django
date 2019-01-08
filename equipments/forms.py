from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import EType, EModel, Lan, Equipments
from location.models import Address

from .choices import *

class ETypeForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Название",
    )

    class Meta:
        model = EType
        fields = ['name']


class EModelForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Название",
    )

    type = forms.ModelChoiceField(
        queryset=EType.objects.all(),
        label='Тип',
    )

    userport_start = forms.IntegerField(
        min_value=1,
        max_value=100,
        label='Порты для пользователя с',
    )

    userport_end = forms.IntegerField(
        min_value=1,
        max_value=100,
        label='Порты для пользователя по',
    )

    note = forms.CharField(
        max_length=200,
        label="Примечания",
    )

    class Meta:
        model = EModel
        fields = ['name', 'type', 'userport_start', 'userport_end', 'note']


class LanForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Название",
    )

    vlan = forms.IntegerField(
        min_value=1,
        max_value=4096,
        label='ID Vlan',
    )

    network = forms.GenericIPAddressField(protocol='IPv4', label='Сеть')

    netmask = forms.ChoiceField(
        choices=NETMASK_CHOICES,
        label="Битовая маска",
        initial='',
        widget=forms.Select(),
        required=True
    )

    gateway = forms.GenericIPAddressField(protocol='IPv4', label='Шлюз')

    class Meta:
        model = Lan
        fields = ['name', 'vlan', 'network', 'netmask', 'gateway']


class EquipmentsForm(forms.ModelForm):

    name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Название",
    )

    estate = forms.ChoiceField(
        label="Состояние",
        choices=STATE_CHOICES,
        initial='',
        widget=forms.Select(),
        required=True
    )

    emodel = forms.ModelChoiceField(
        queryset=EModel.objects.all(),
        label="Модель",
        required=True,
    )

    location = TreeNodeChoiceField(
        label="Адрес",
        queryset=Address.objects.all(),
        level_indicator=u'+--'
    )

    adr_entrance = forms.CharField(label="Подъезд",)
    adr_floor = forms.CharField(label="Этаж",)
    ip = forms.GenericIPAddressField(protocol='IPv4', label='IP адрес')

    mac = forms.CharField(
        min_length=12,
        max_length=20,
        label="MAC адрес",
    )

    serial = forms.CharField(
        min_length=6,
        max_length=50,
        label="Серийный номер",
    )

    note = forms.CharField(label="Примечание",  widget=forms.Textarea(),)

    class Meta:
        model = Equipments
        fields = [
            'name',
            'estate',
            'emodel',
            'location',
            'adr_entrance',
            'adr_floor',
            'ip',
            'mac',
            'serial',
            'note'
        ]