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

def menu(request, menuid):
    mydish=Dish.objects.filter(name=menuid).first()
    Ing=mydish.ingredients.all()
    rate=Rating.objects.filter(dish_id=mydish.id).all()
    if request.user.role == User.Role.CLIENT:
        if request.method == "POST":
            form = RatingForm(request.POST)
            if form.is_valid():
                form.save(dish_id=mydish, client_id=request.user)
                return HttpResponseRedirect(reverse("main:search"))
            else:
                for error in list(form.errors.values()):
                    print(request, error)
        else:
            form = RatingForm()

        return render(request, "main/menuclient.html", {
            "menu": menuid,
            "ingredients": Ing,
            "ratings": rate,
            "form": form
        })
    else:
        return render(request, "main/menu.html", {
            "menu": menuid,
            "ingredients": Ing,
            "ratings": rate
        })

