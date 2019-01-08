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

from .forms import (
    ETypeForm,
    EModelForm,
    LanForm,
    EquipmentsForm,
)

from .models import (
    Equipments,
    EType,
    EModel,
    Lan,
    Port,
    Catalog_Lan,
)

# Type CRUD ------------------------------------------------------------------------------------------------------------
class TypeList(ListView):
    model = EType
    template_name = 'equipments/type/list.html'
    paginate_by = 25


class TypeCreate(CreateView):
    model = EType
    template_name = 'equipments/common/form.html'
    form_class = ETypeForm
    success_url = reverse_lazy('equipments:type-list')


class TypeUpdate(UpdateView):
    model = EType
    template_name = 'equipments/common/form.html'
    form_class = ETypeForm
    success_url = reverse_lazy('equipments:type-list')


class TypeDelete(DeleteView):
    model = EType
    template_name = 'equipments/common/delete.html'
    success_url = reverse_lazy('equipments:type-list')


# Model CRUD -----------------------------------------------------------------------------------------------------------
class ModelList(ListView):
    model = EModel
    template_name = 'equipments/model/list.html'
    paginate_by = 25


class ModelCreate(CreateView):
    model = EModel
    template_name = 'equipments/common/form.html'
    form_class = EModelForm
    success_url = reverse_lazy('equipments:model-list')


class ModelUpdate(UpdateView):
    model = EModel
    template_name = 'equipments/common/form.html'
    form_class = EModelForm
    success_url = reverse_lazy('equipments:model-list')


class ModelDelete(DeleteView):
    model = EModel
    template_name = 'equipments/common/delete.html'
    success_url = reverse_lazy('equipments:model-list')


# Lan CRUD -------------------------------------------------------------------------------------------------------------
class LanList(ListView):
    model = Lan
    template_name = 'equipments/lan/list.html'
    paginate_by = 25


class LanCreate(CreateView):
    model = Lan
    template_name = 'equipments/common/form.html'
    form_class = LanForm
    success_url = reverse_lazy('equipments:lan-list')


class LanUpdate(UpdateView):
    model = Lan
    template_name = 'equipments/common/form.html'
    form_class = LanForm
    success_url = reverse_lazy('equipments:lan-list')


class LanDelete(DeleteView):
    model = Lan
    template_name = 'equipments/common/delete.html'
    success_url = reverse_lazy('equipments:lan-list')


# Equipments
class EquipmentsList(ListView):
    template_name = 'equipments/list.html'
    model = Equipments
    paginate_by = 25


class EquipmentsCreate(CreateView):
    model = Equipments
    template_name = 'equipments/common/form.html'
    form_class = EquipmentsForm
    success_url = reverse_lazy('equipments:equipments-list')


class EquipmentsUpdate(UpdateView):
    model = Equipments
    template_name = 'equipments/common/form.html'
    form_class = EquipmentsForm
    success_url = reverse_lazy('equipments:equipments-list')


class EquipmentsDelete(DeleteView):
    model = Equipments
    template_name = 'equipments/common/delete.html'
    success_url = reverse_lazy('equipments:equipments-list')


class PortList(ListView):
    """
    Port
    """
    template_name = 'equipments/port/list.html'
    model = Port

    def get_queryset(self):
        return self.model.objects.filter(equipments_id=self.kwargs['id'])
