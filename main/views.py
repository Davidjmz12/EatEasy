from math import ceil

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import Restaurant, User
from main.forms import RatingForm
from main.models import Dish, Rating


# Create your views here.
def index(request):
    if not request.user.is_superuser:
        if request.method == "POST":
            return HttpResponseRedirect(
                reverse("main:search", kwargs={"location": request.POST["location"]})
            )
        else:
            return render(request, "main/index.html")
    else:
        return HttpResponseRedirect(reverse("super:index"))


def subsetCeliac(rest, cel):
    new_rest = []
    for oneRest in rest:
        my_dishes = oneRest.my_dishes.all()
        celiacArray = [item.celiac for item in my_dishes]
        if not cel or (cel and any(celiacArray)):
            new_rest.append(oneRest)

    return new_rest


def subsetVegan(rest, veg):
    new_rest = []
    for oneRest in rest:
        my_dishes = oneRest.my_dishes.all()
        veganArray = [item.vegan for item in my_dishes]
        if not veg or (veg and any(veganArray)):
            new_rest.append(oneRest)

    return new_rest


def subsetVegetarian(rest, veget):
    new_rest = []
    for oneRest in rest:
        my_dishes = oneRest.my_dishes.all()
        vegetarianArray = [item.vegetarian for item in my_dishes]
        if not veget or (veget and any(vegetarianArray)):
            new_rest.append(oneRest)

    return new_rest


def subsetCity(rest, loc):
    new_rest = []
    for oneRest in rest:
        print(oneRest.precise_location, loc)
        if oneRest.precise_location == loc:
            new_rest.append(oneRest)
    return new_rest


def subsetPrice(rest, maxSlider):
    new_rest = []
    for oneRest in rest:
        my_dishes = [item.price for item in oneRest.my_dishes.all()]
        avgPrice = sum(my_dishes) / len(my_dishes)
        if avgPrice <= maxSlider:
            print(avgPrice, maxSlider)
            new_rest.append(oneRest)

    return new_rest


def queryRestaurants(cel, vegan, veget, loc, maxSlider):
    rest = Restaurant.objects.all()
    rest = subsetVegan(rest, vegan)
    rest = subsetVegetarian(rest, veget)
    rest = subsetCeliac(rest, cel)
    rest = subsetCity(rest, loc)
    rest = subsetPrice(rest, maxSlider)
    return rest


def getMax(restaurants):
    avg_prices = []
    for oneRest in restaurants:
        my_dishes = [item.price for item in oneRest.my_dishes.all()]
        avg_prices.append(sum(my_dishes) / len(my_dishes))
    try:
        maxS = max(avg_prices)
    except:
        maxS = 0
    return maxS


def search(request, location):
    cel = request.POST.get("celiac", "off") == "on"
    veget = request.POST.get("vegetarian", "off") == "on"
    vegan = request.POST.get("vegan", "off") == "on"
    loc = request.POST.get("location", location)
    maxSlider = int(request.POST.get("maxValue", 0))

    if request.method == "POST":
        restaurants = queryRestaurants(cel, vegan, veget, loc, maxSlider)
    else:
        restaurants = Restaurant.objects.all()

    maxPrice = getMax(Restaurant.objects.all())
    return render(
        request,
        "main/search.html",
        {
            "restaurants": restaurants,
            "max": ceil(maxPrice),
            "location": loc,
            "cel": cel,
            "veget": veget,
            "vegan": vegan,
        },
    )


def restaurant(request, user_id):
    res = Restaurant.objects.filter(user_id=user_id).first()
    return render(
        request,
        "main/restaurant.html",
        {"restaurant": res, "dishes": res.my_dishes.all()},
    )


def restaurant_info(request, user_id):
    res = Restaurant.objects.filter(user_id=user_id).first()
    return render(request, "main/restaurant-info.html", {"restaurant": res})


def filters(request):
    return render(request, "main/layout-filters.html")


def menu(request, menuid):
    mydish = Dish.objects.filter(name=menuid).first()
    Ing = mydish.ingredients.all()
    rate = Rating.objects.filter(dish_id=mydish.id).all()
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

        return render(
            request,
            "main/menuclient.html",
            {"menu": menuid, "ingredients": Ing, "ratings": rate, "form": form},
        )
    else:
        return render(
            request,
            "main/menu.html",
            {"menu": menuid, "ingredients": Ing, "ratings": rate},
        )
