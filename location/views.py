from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Address
from .forms import AdrForm


class List(View):
    template_name = "location/address_list.html"
    model = Address
    paginate = 25

    def get(self, request, *args, **kwargs):
        parents = [{'id': 0, 'name': 'root'}]

        _id = kwargs.get('id')

        if (_id is not None) and (_id > 0):
            # Get all parents
            q = Address.objects.filter(parent_id=_id)
            pr = Address.objects.get(id=_id)

            for parent in pr.get_ancestors(ascending=False, include_self=False):
                parents.append({'id': parent.id, 'name': parent.name})

            parents.append({'id': pr.id, 'name': pr.name})

        else:
            # Get root tree
            q = Address.objects.filter(level=0)

        # Pagination
        paginator = Paginator(q, self.paginate)
        page = self.request.GET.get('page')

        try:
            adr = paginator.page(page)
        except PageNotAnInteger:
            adr = paginator.page(1)
        except EmptyPage:
            adr = paginator.page(paginator.num_pages)

        # Context
        context = {
            'object_list': adr,
            'parents': parents,
        }

        return render(request, self.template_name, context)


class Create(View):
    """
        Class that allows you to new a Address object.
    """
    template_name = "location/address_form_create.html"
    model = Address
    form = AdrForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form(),})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            parent_id = kwargs.get('id')

            model_adr = self.model()

            model_adr.name = form.cleaned_data['name']
            model_adr.parent_id = parent_id
            model_adr.save()

            return redirect('location:list', id=parent_id)

        context = {"form": form}
        return render(request, self.template_name, context)


class Update(View):
    """
        Class that allows you to update a Address object.
    """
    template_name = "location/address_form_update.html"
    model = Address
    form = AdrForm

    def get(self, request, *args, **kwargs):
        adr = get_object_or_404(self.model, id = kwargs.get('id'))
        return render(request, self.template_name, {'form': self.form(initial={'name': adr.name,})})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            adr = get_object_or_404(self.model, id=kwargs.get('id'))
            adr.name = form.cleaned_data['name']
            adr.save()

            return redirect('location:list', id=adr.parent_id)

        context = {"form": form}
        return render(request, self.template_name, context)


class Delete(DeleteView):
    """
    Class that allows you to delete a Address object.
    """
    model = Address
    success_url = reverse_lazy('location:list')

    def get_object(self):
        id_ = self.kwargs.get("id")
        adr = get_object_or_404(Address, id=id_)

        self.success_url = reverse_lazy('location:list', kwargs={'id': adr.parent_id})
        return adr
