from django import forms
from .models import Chef,Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields='__all__'


class ChefForm(forms.ModelForm):
    class Meta:
        model=Chef
        fields='__all__'

