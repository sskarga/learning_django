from django import forms
from .models import Address


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

    parent_id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Address
        fields = ['name']
