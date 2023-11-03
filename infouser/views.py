from datetime import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from infouser.forms import DishForm, ResForm
from main.models import Rating, Dish, Ingredient
from login.models import *


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


def news(request):
    news = [
        Rating(2, "Muy bueno", 4, 4)
    ]  ##request.user.Restaurants.my_dishes ####deberia ser mis rating
    return render(request, "infouser/news.html", {"news": news})


def client(request):
    return None

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
    ##rate=Rating.objects.get(dish=mydish.id)
    return render(request, "infouser/menu.html", {
        "menu": menuid,
        "ingredients": Ing,
        ##"ratings": rate
    })


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