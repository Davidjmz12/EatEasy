from django.shortcuts import render
from login.models import Restaurant
from main.models import Dish
from django import forms


class RestaurantForm(forms.Form):
    Restaurants = Restaurant.objects.all()

    selected_restaurant = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'form_restaurant'}),
                                          required=False)


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def search(request):
    form = RestaurantForm()
    return render(request, "main/search.html", {
        "restaurants": Restaurant.objects.all(),
        "form": form
    })


def restaurant(request, user_id):
    res = Restaurant.objects.filter(user_id=user_id).first()
    return render(request, "main/restaurant.html", {
        "restaurant": res,
        "dishes": res.my_dishes.all()
    })


def restaurant_info(request):
    return render(request, "main/restaurant-info.html")


def filters(request):
    return render(request, "main/layout-filters.html")
