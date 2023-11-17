from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("main:index"))
    else:
        return render(request, "")
