from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from login.models import User
from login.form import UserRegistrationForm, RestaurantRegistrationForm


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login:login"))
    else:
        return HttpResponseRedirect(reverse("main:index"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("login:index"))
        else:
            return render(request, "login/login.html", {
                "message": "Invalid credentials"
            })
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:index"))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("main:index"))
    else:
        return render(request, "login/register.html")


def registerRest(request):
    if request.method == "POST":
        form = RestaurantRegistrationForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            login(request, restaurant)
            return HttpResponseRedirect(reverse("main:index"))
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = RestaurantRegistrationForm()

    form.fields['web_page'].widget.attrs['class'] = "input-form"
    form.fields['precise_location'].widget.attrs['class'] = "input-form"
    form.fields['city'].widget.attrs['class'] = "input-form"
    form.fields['phone_number'].widget.attrs['class'] = "input-form"
    form.fields['description'].widget.attrs['class'] = "input-form"
    form.fields['rest_name'].widget.attrs['class'] = "input-form"
    form.fields['email'].widget.attrs['class'] = "input-form"
    form.fields['first_name'].widget.attrs['class'] = "input-form"
    form.fields['last_name'].widget.attrs['class'] = "input-form"
    form.fields['username'].widget.attrs['class'] = "input-form"
    form.fields['password1'].widget.attrs['class'] = "input-form"
    form.fields['password2'].widget.attrs['class'] = "input-form"

    return render(
        request=request,
        template_name="login/registerRest.html",
        context={"form": form}
    )


def registerUser(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()

    form.fields['email'].widget.attrs['class'] = "input-form"
    form.fields['first_name'].widget.attrs['class'] = "input-form"
    form.fields['last_name'].widget.attrs['class'] = "input-form"
    form.fields['username'].widget.attrs['class'] = "input-form"
    form.fields['password1'].widget.attrs['class'] = "input-form"
    form.fields['password2'].widget.attrs['class'] = "input-form"
    return render(
        request=request,
        template_name="login/registerUser.html",
        context={"form": form}
    )
