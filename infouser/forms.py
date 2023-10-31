from django import forms
from django.forms import ModelForm

from login.models import Restaurant
from main.models import Dish


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'restaurant', 'price']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
        }

class ResForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['rest_name', 'city', 'precise_location', 'phone_number', 'description', 'web_page']