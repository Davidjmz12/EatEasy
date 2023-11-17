from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from infouser.models import Notification
from login.models import Restaurant, User


# Create your views here.
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("main:index"))
    else:
        notif = request.user.my_received_not.all()
        return render(request, "super/index.html",
                      context={"notifications": notif})


def management(request):
    restaurants = Restaurant.objects.all()
    return render(request, "super/management.html",
                  {"restaurants": restaurants})


def deleteRes(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return HttpResponseRedirect(reverse("super:management"))


def oneRestaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    print(restaurant.rest_name)
    return render(request, "super/oneRestaurant.html",
                  {"restaurant": restaurant})


def notification(request, pk):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        emissor = User.objects.get(pk=request.user.pk)
        receiver = User.objects.get(pk=pk)
        notif = Notification(emissor=emissor, receiver=receiver, description=description, title=title)
        notif.save()
        return HttpResponseRedirect(reverse("super:management"))
    return render(request, "super/notification.html")
