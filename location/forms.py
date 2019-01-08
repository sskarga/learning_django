from django import forms
from .models import Address
from django.urls import reverse


class AdrForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Название",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }
        )
    )

    class Meta:
        model = Address
        fields = ['name']

    def get_absolute_url(self):
        return reverse("location:list", kwargs={"id": self.id})
