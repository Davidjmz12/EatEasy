from datetime import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from infouser.forms import DishForm, ResForm
from infouser.forms import DishForm
from infouser.models import Notification
from main.models import Rating, Ingredient
from infouser.forms import DishForm, ResForm, ClientForm
from main.models import Rating, Dish
from login.models import *
import json

# Create your views here.
def index(request):
    if request.user.role == User.Role.RESTAURANT:
        return HttpResponseRedirect(reverse("infouser:restaurant"))
    elif request.user.role == User.Role.CLIENT:
        return HttpResponseRedirect(reverse("infouser:client"))
    else:
        return HttpResponse("InfoUser")


def restaurant(request):
    dishes = request.user.Restaurants.my_dishes.all()
    return render(request, "infouser/restaurant.html", {
        "dishes": dishes,
        "restaurant": Restaurant.objects.filter(user_id=request.user.Restaurants.user_id).first()
    })


def newMenu(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save(restaurant=request.user.Restaurants)
            return HttpResponseRedirect(reverse("infouser:restaurant"))
        else:
            for error in list(form.errors.values()):
                print(request, error)
            return render(request, "infouser/newmenu.html", {"form": form})
    else:
        form = DishForm()

    return render(
        request,
        "infouser/newmenu.html",
        {
            "form": form
        },
    )



def client(request):
    cliente = Client.objects.get(id=request.user.id)
    form = ClientForm(instance=cliente)
    return render(request, "infouser/client_info.html", {
        "form": form
    })

def update_info_client(request):
    cliente =  Client.objects.get(pk=request.user.id)
    form = ClientForm(request.POST, instance=cliente)
    if form.is_valid():
        form.save()
    return render(request, "main/index.html")


def changeinfo(request):
    res = Restaurant.objects.filter(user_id=request.user.Restaurants.user_id).first()
    form = ResForm(instance=res)
    return render(request, "infouser/changeinfo.html", {
        "restaurant": res,
        "form": form
    })

def update_info(request):
    res =  Restaurant.objects.get(pk=request.user.Restaurants.user_id)
    form = ResForm(request.POST, instance=res)
    if form.is_valid():
        form.save()
    dishes=request.user.Restaurants.my_dishes.all()
    return render(request, "infouser/restaurant.html", {
        "dishes": dishes,
        "restaurant": Restaurant.objects.filter(user_id=request.user.Restaurants.user_id).first()
    })


def menu(request, menuid):
    mydish=Dish.objects.filter(name=menuid, restaurant_id=request.user.Restaurants.user_id).first()
    Ing=mydish.ingredients.all()
    rate=Rating.objects.filter(dish_id=mydish.id).all()
    return render(request, "infouser/menu.html", {
        "menu": menuid,
        "ingredients": Ing,
        "ratings": rate
    })


def notification(request):
    notif = request.user.my_received_not.all()
    return render(request, "infouser/notifications.html",
                  context={"notifications": notif})


def infoNot(request, notification_id):
    notif = Notification.objects.get(pk=notification_id)
    notif.read = True
    notif.save()
    print(notif)
    return render(request, "infouser/oneNotification.html",
                  context={"notification": notif})


def deleteNotification(request, notification_id):
    notif = Notification.objects.get(pk=notification_id)
    notif.delete()
    return HttpResponseRedirect(reverse("infouser:notifications"))


def changemenu(request, menuid):
    dish = request.user.Restaurants.my_dishes.all()
    mydish= dish.filter(name=menuid).first()
    form = DishForm(instance=mydish)
    return render(request, "infouser/changemenu.html", {
        "menu": menuid,
        "form": form
    })


def update_menu(request, menuid):
    dish = Dish.objects.get(restaurant=request.user.Restaurants.user_id,name=menuid)
    form = DishForm(request.POST, instance=dish)
    if form.is_valid():
        form.save(restaurant=request.user.Restaurants)
    return render(request, "infouser/restaurant.html", {
        "dishes": request.user.Restaurants.my_dishes.all(),
        "restaurant": Restaurant.objects.filter(user_id=request.user.Restaurants.user_id).first()
    })


def statistics(request):
    Ing = Ingredient.objects.all()
    names = []
    number = []
    for i in Ing:
        n = len(i.dishes_with.all())
        names.append(i.name)
        number.append(n)

    zipp = zip(names, number)
    return render(request, "infouser/statistics.html", {
        "ingredients": json.dumps(names),
        "numbers": json.dumps(number),
        "zip": zipp
    })