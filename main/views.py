import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import Restaurant, User
from main.forms import RatingForm
from main.models import Dish, Rating


# Create your views here.
def index(request):
    if not request.user.is_superuser:
        return render(request, "main/index.html")
    else:
        return HttpResponseRedirect(reverse("super:index"))


def search(request):
    return render(request, "main/search.html", {
        "restaurants": Restaurant.objects.all()
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


def menu(request, rest, menuid):
    restaurant = Restaurant.objects.filter(rest_name=rest).first()
    mydish=Dish.objects.filter(name=menuid, restaurant=restaurant).first()
    Ing=mydish.ingredients.all()
    rate=Rating.objects.filter(dish_id=mydish.id).all()
    if not request.user.is_authenticated:
        return render(request, "main/menu.html", {
            "menu": menuid,
            "ingredients": Ing,
            "ratings": rate,
            "form": None
        })
    if request.user.role == User.Role.CLIENT:
        if request.method == "POST":
            form = RatingForm(request.POST)
            if form.is_valid():
                form.save(dish_id=mydish, client_id=request.user, date=datetime.datetime.now())
                return HttpResponseRedirect(reverse("main:search"))
            else:
                for error in list(form.errors.values()):
                    print(request, error)
        else:
            form = RatingForm()

        form.fields['rate'].widget.attrs['class'] = "input-form"
        form.fields['comment'].widget.attrs['class'] = "input-form"
        return render(request, "main/menu.html", {
            "menu": menuid,
            "ingredients": Ing,
            "ratings": rate,
            "form": form
        })
    else:
        return render(request, "main/menu.html", {
            "menu": menuid,
            "ingredients": Ing,
            "ratings": rate,
            "form": None
        })

