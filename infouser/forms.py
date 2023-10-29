from django import forms
from django.forms import ModelForm

from main.models import Dish


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'restaurant', 'price']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
        }
