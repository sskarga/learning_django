from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

from .models import (
    Equipments,
    EType,
    EState,
    EModel,
    Lan,
    Port,
    Catalog_Lan,
)


class TypeList(ListView):
    """
    Type
    """
    template_name = 'equipments/type/list.html'


class StateList(ListView):
    """
    State
    """
    template_name = 'equipments/state/list.html'


class ModelList(ListView):
    """
    Model
    """
    template_name = 'equipments/model/list.html'
    paginate_by = 25


class LanList(ListView):
    """
    Lan
    """
    template_name = 'equipments/lan/list.html'
    model = Lan
    paginate_by = 25

    def get_queryset(self):

        object_list = self.model.objects.all()

        if ('equipments_id' in self.request.GET) and self.request.GET['equipments_id'].strip():
            eq_id = self.request.GET.get('equipments_id')
            object_list = self.model.objects.filter(
                catalog_lan__equipments_id=eq_id)

        if ('id' in self.request.GET) and self.request.GET['id'].strip():
            _id = self.request.GET.get('id')
            object_list = self.model.objects.filter(id=_id)

        return object_list


class EquipmentsList(ListView):
    """
    Equipments
    """
    template_name = 'equipments/list.html'
    model = Equipments
    paginate_by = 25

    def get_queryset(self):
        object_list = self.model.objects.all()

        _id = self.request.GET.get('id')
        location_id = self.request.GET.get('location_id')
        vlan_id = self.request.GET.get('vlan_id')

        if not (location_id is None):
            object_list = self.model.objects.filter(
                location_id=int(location_id))

        if not (vlan_id is None):
            object_list = self.model.objects.filter(catalog_lan__lan=vlan_id)

        if not (_id is None):
            object_list = self.model.objects.filter(id=int(_id))

        return object_list


class PortList(ListView):
    """
    Port
    """
    template_name = 'equipments/port/list.html'
    model = Port

    def get_queryset(self):
        return self.model.objects.filter(equipments_id=self.kwargs['id'])
