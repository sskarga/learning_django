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
    Equipments_Type,
    Equipments_State,
    Equipments_Model,
    Lan,
)

# Type
class TypeList(ListView):
    template_name = 'equipments/type/list.html'
    queryset = Equipments_Type.objects.all()

# State
class StateList(ListView):
    template_name = 'equipments/state/list.html'
    queryset = Equipments_State.objects.all()    

# Model
class ModelList(ListView):
    template_name = 'equipments/model/list.html'
    queryset = Equipments_Model.objects.all() 
    paginate_by = 25

# Lan
class LanList(ListView):
    template_name = 'equipments/lan/list.html'
    model = Lan
    # queryset = Lan.objects.all() 
    paginate_by = 25

    def get_queryset(self):

        location_id = self.request.GET.get('location_id')
        
        if location_id is None:
            object_list = self.model.objects.all()
        else:
            object_list = self.model.objects.filter(location_id = int(location_id))
        return object_list

# Equipments
class EquipmentsList(ListView):
    template_name = 'equipments/list.html'
    model = Equipments
    paginate_by = 25

    def get_queryset(self):
        object_list = self.model.objects.all()

        _id = self.request.GET.get('id')
        location_id = self.request.GET.get('location_id') 
        vlan_id = self.request.GET.get('vlan_id')
            
        if not (location_id is None):
            object_list = self.model.objects.filter(location_id = int(location_id))
        
        if not (vlan_id is None):    
            object_list = self.model.objects.filter(vlan_id = int(vlan_id))
        
        if not (_id is None):    
            object_list = self.model.objects.filter(id = int(_id))

        return object_list