from django import forms

from main.models import Dish


class DishForm(forms.Form):
    class Meta:
        model= Dish
        fields=['name', 'ingredients', 'restaurant', 'price']
        widgets={
            'ingredients': forms.CheckboxSelectMultiple,
        }
