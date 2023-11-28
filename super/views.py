import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from infouser.models import Notification
from login.models import Restaurant, User
from main.models import Ingredient, Dish
from collections import Counter

# Create your views here.
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("main:index"))
    else:
        notif = request.user.my_received_not.all()
        return render(request, "super/index.html", context={"notifications": notif})


def management(request):
    restaurants = Restaurant.objects.all()
    return render(request, "super/management.html", {"restaurants": restaurants})


def deleteRes(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return HttpResponseRedirect(reverse("super:management"))


def oneRestaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    print(restaurant.rest_name)
    return render(request, "super/oneRestaurant.html", {"restaurant": restaurant})


def notification(request, pk):
    if request.method == "POST":
        title = request.POST["title"].strip()
        if title != "":
            title = title[0].upper() + title[1:]
        description = request.POST["description"].strip()
        if description != "":
            description = description[0].upper() + title[1:]
        emissor = User.objects.get(pk=request.user.pk)
        receiver = User.objects.get(pk=pk)
        if title == "" or description == "":
            return render(request, "super/notification.html",
                          context={"err": "Inputs cannot be empty",
                                   "title": title,
                                    "description": description})
        elif len(title) > 30:
            return render(request, "super/notification.html",
                          context={"err": "Title max length is 30",
                                   "title": title,
                                   "description": description})
        elif len(description) > 200:
            return render(request, "super/notification.html",
                          context={"err": "Description max length is 200",
                                   "title": title,
                                   "description": description})
        else:
            notif = Notification(
                emissor=emissor, receiver=receiver, description=description, title=title
            )
            notif.save()
            return HttpResponseRedirect(reverse("super:management"))
    else:
        return render(request, "super/notification.html")


def ingredients(request):
    if request.method == "POST":
        allData = [int(item) for item in request.POST.getlist("values")]
        for pk in allData:
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.delete()
        return HttpResponseRedirect(reverse("super:ingredients"))
    else:
        ingredientsAll = Ingredient.objects.all()
        return render(
            request, "super/ingredients.html", context={"ingredients": ingredientsAll}
        )


def addIng(request):
    if request.method == "POST":
        name = request.POST["name"].strip().capitalize()
        try:
            if name == "":
                return render(
                    request, "super/addIngredient.html", context={"warningSintax": True}
                )
            else:
                Ingredient(name=name).save()
        except:
            return render(
                request, "super/addIngredient.html", context={"warning": True}
            )

        if "back" in request.POST:
            return HttpResponseRedirect(reverse("super:ingredients"))
        else:
            return HttpResponseRedirect(reverse("super:addIng"))
    else:
        return render(request, "super/addIngredient.html")


def getNumberNamesPrice(prices):
    maxPrice = max(prices)
    number = []
    names = []
    for m in range(int(maxPrice / 5) + 1):
        n = 0
        for i in range(len(prices)):
            if 5 * (m + 1) > prices[i] >= 5 * m:
                n = n + 1
        names.append(5 * m)
        number.append(n)
    return number, names


def getRenderGraph(typeGraph, filterRest=None):
    number = []
    names = []
    if typeGraph == "price":
        Ing = Dish.objects.filter(restaurant=filterRest).all() if filterRest else Dish.objects.all()
        prices = [oneIng.price for oneIng in Ing]
        number, names = getNumberNamesPrice(prices)
    elif typeGraph == "filter":
        Ing = Dish.objects.filter(restaurant=filterRest).all() if filterRest else Dish.objects.all()
        names = ["vegan", "vegetarian", "nuts_free", "lactose_free", "celiac"]
        number = [len(Ing.filter(**{filter_: True}).all()) for filter_ in names]
    elif typeGraph == "city":
        res = Restaurant.objects.all()
        city_counter = Counter(r.city for r in res)
        names, number = zip(*city_counter.items())
    elif typeGraph == "ingredients":
        Ing = Ingredient.objects.all()
        if filterRest:
            number = [len(oneIng.dishes_with.filter(restaurant=filterRest).all()) for oneIng in Ing]
        else:
            number = [len(oneIng.dishes_with.all()) for oneIng in Ing]
        names = [_.name for _ in Ing]
    zipp = zip(names, number)
    return names, number, zipp


def statistics(request, typeGraph):
    names, number, zipp = getRenderGraph(typeGraph)
    return render(
        request,
        "super/statistics.html",
        {
            "ingredients": json.dumps(names),
            "numbers": json.dumps(number),
            "zip": zipp,
            "type": typeGraph,
        },
    )
