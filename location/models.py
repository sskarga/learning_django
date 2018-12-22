from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Address(MPTTModel):
    """
        Class that manages the address model fields
    """
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('location:update', kwargs={'pk': self.pk})
