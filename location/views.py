from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Address
from .forms import AdrForm

# Create your views here.
class Index(TemplateView):
    """
    Class that shows the start template.
    """
    template_name = "location/index.html"


class List(ListView):
    """
    Class that lists the Address objects.
    """
    model = Address
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        # Query bild
        parents = [{'id': 0, 'name': 'root'}]

        if ('id' in self.kwargs) and (int(self.kwargs['id']) > 0):
            q = Address.objects.filter(parent_id=self.kwargs['id'])
            pr = Address.objects.get(id=self.kwargs['id'])

            for parent in pr.get_ancestors(ascending=True, include_self=False):  # ascending=False,
                parents.append({'id': parent.id, 'name': parent.name})

            parents.append({'id': pr.id, 'name': pr.name})

        else:
            q = Address.objects.filter(level=0)

        # Pagination
        paginator = Paginator(q, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            adr = paginator.page(page)
        except PageNotAnInteger:
            adr = paginator.page(1)
        except EmptyPage:
            adr = paginator.page(paginator.num_pages)

        # Context
        context['object_list'] = adr
        context['paginator'] = adr.paginator
        context['parent'] = parents[-1]
        context['parents'] = parents
        return context


class Create(CreateView):
    """
    Class that allows you to create and save a Person object.
    """
    model = Address
    form_class = AdrForm
    success_url = reverse_lazy('location:list')

    def get_initial(self):
        initial = super(Create, self).get_initial()
        parent_id = self.kwargs.get('id')
        self.success_url = reverse_lazy('location:list', kwargs={'id': parent_id})

        initial.update({
                    'parent':parent_id,
                        })
        return initial



class Update(UpdateView):
    """
    Class that allows you to update the data of a Person object.
    """
    model = Address
    form_class = AdrForm
    success_url = reverse_lazy('location:list')

    def get_object(self):
        id_ = self.kwargs.get("id")
        adr = get_object_or_404(Address, id=id_)

        self.success_url = reverse_lazy('location:list', kwargs={'id': adr.parent_id})
        return adr


class Delete(DeleteView):
    """
    Class that allows you to delete a Person object.
    """
    model = Address
    success_url = reverse_lazy('location:list')

    def get_object(self):
        id_ = self.kwargs.get("id")
        adr = get_object_or_404(Address, id=id_)

        self.success_url = reverse_lazy('location:list', kwargs={'id': adr.parent_id})
        return adr
