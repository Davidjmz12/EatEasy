from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.urls import reverse

from infouser.forms import DishForm
from main.models import Rating


# Create your views here.
def index(request):
    return HttpResponse("InfoUser")

def restaurant(request):
    if(request.user.is_authenticated()):
        dishes = request.user.Restaurants.my_dishes.all()
        return render(request, "infouser/restaurant.html", {
            "dishes": dishes
        })
    else:
        return render(request, "main/search.html")

def newmenu(request):
    if request.method=="POST":
        form=DishForm(request.POST)
        if form.is_valid():
            dish = form.cleaned_data["dish"]
            request.session["dish"] += [dish]
            return HttpResponse(reverse("infouser:restaurant"))
        else:
            for error in list(form.errors.values()):
                print(request, error)
            return render(request, "infouser/newmenu.html", {
                "form": form
            })

    return render(request, "infouser/newmenu.html",{
        #"form":form
    })

def news(request):
    news = [Rating(2,'Muy bueno',4,4)]##request.user.Restaurants.my_dishes ####deberia ser mis rating
    return render(request, "infouser/news.html", {
        "news": news
    })