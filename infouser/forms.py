from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from login.models import Restaurant
from main.models import Dish


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'price', 'vegan', 'vegetarian', 'celiac', 'nuts_free', 'lactose_free', 'dish_image']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
        }

    def save(self, commit=True, restaurant=None):
        dish = super(DishForm, self).save(commit=False)
        if commit and restaurant:
            dish.restaurant = restaurant
            dish.save()
            selected_ingredients = self.cleaned_data['ingredients']
            dish.ingredients.set(selected_ingredients)
        return dish

class ClientForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']



class ResForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['rest_name', 'city', 'precise_location', 'phone_number', 'description', 'web_page']

