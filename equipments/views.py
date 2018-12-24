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
    Equipments_Type,
    Equipments_State,
    Equipments_Model,
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

# Equipments
class EquipmentsList(ListView):
    pass