from django import forms
from django.forms import ModelForm

from login.models import Restaurant
from main.models import Dish


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'price', 'vegan', 'vegetarian','celiac', 'dish_image']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
        }

    def save(self, commit=True, restaurant=None):
        dish = super(DishForm, self).save(commit=False)
        if commit and restaurant:
            dish.restaurant = restaurant
            dish.save()
        return dish


class ResForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['rest_name', 'city', 'precise_location', 'phone_number', 'description', 'web_page']

