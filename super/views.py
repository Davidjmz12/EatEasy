from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from infouser.models import Notification
from login.models import Restaurant


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
