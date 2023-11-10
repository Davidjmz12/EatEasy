from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import Restaurant


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def search(request, city):
    return render(request, "main/search.html", {
        "restaurants": Restaurant.objects.filter(city=city)
    })


def restaurant(request, user_id):
    res = Restaurant.objects.filter(user_id=user_id).first()
    return render(request, "main/restaurant.html", {
        "restaurant": res,
        "dishes": res.my_dishes.all()
    })


def restaurant_info(request, user_id):
    res = Restaurant.objects.filter(user_id=user_id).first()
    return render(request, "main/restaurant-info.html", {
        "restaurant": res
    })


def filters(request):
    return render(request, "main/layout-filters.html")
