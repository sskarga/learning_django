from django import forms
from .models import Address


class AdrForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=50, label="Название", help_text="Введите новое место")
    #parent_id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Address
        fields = ['name', 'parent']