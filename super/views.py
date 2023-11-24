import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from infouser.models import Notification
from login.models import Restaurant, User
from main.models import Ingredient, Dish


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
        title = request.POST["title"]
        description = request.POST["description"]
        emissor = User.objects.get(pk=request.user.pk)
        receiver = User.objects.get(pk=pk)
        notif = Notification(
            emissor=emissor, receiver=receiver, description=description, title=title
        )
        notif.save()
        return HttpResponseRedirect(reverse("super:management"))
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
        name = request.POST["name"]
        try:
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


def statistic_price(request):
    Ing = Dish.objects.all()
    prices = []
    number = []
    names = []
    maximo=0
    for i in Ing:
        if(maximo<i.price):
            maximo=i.price
        prices.append(i.price)

    for m in range(int(maximo/5)+1):
        n = 0
        for i in range(len(prices)):
            if(prices[i]<5*(m+1) and prices[i]>=5*m):
                n=n+1

        names.append(5*m)
        number.append(n)

    zipp = zip(names, number)
    return render(request, "super/statistics.html", {
        "ingredients": json.dumps(names),
        "numbers": json.dumps(number),
        "zip": zipp
    })

def statistic_filter(request):
    Ing = Dish.objects.all()
    number = []
    names = ["vegan","vegetarian","nuts free", "lactose free", "gluten free"]
    n=len(Ing.filter(vegan=True).all())
    number.append(n)
    n=len(Ing.filter(vegetarian=True).all())
    number.append(n)
    n=len(Ing.filter(nuts_free=True).all())
    number.append(n)
    n=len(Ing.filter(lactose_free=True).all())
    number.append(n)
    n=len(Ing.filter(celiac=True).all())
    number.append(n)

    zipp = zip(names, number)
    return render(request, "super/statistics.html", {
        "ingredients": json.dumps(names),
        "numbers": json.dumps(number),
        "zip": zipp
    })

def statistic_city(request):
    res=Restaurant.objects.all()
    cities=[]
    number=[]
    for r in res:
        if r.city not in cities:
            cities.append(r.city)
            n=len(res.filter(city=r.city))
            number.append(n)

    zipp = zip(cities, number)
    return render(request, "super/statistics.html", {
        "ingredients": json.dumps(cities),
        "numbers": json.dumps(number),
        "zip": zipp
    })
