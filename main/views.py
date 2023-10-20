from django.shortcuts import render
from login.models import *

# All the information for one restaurant
class Restaurante:
    def __init__(self, name, description, img):
        self.name = name
        self.description = description
        self.img = img


class Dish:
    def __init__(self, name, price, stars, ingredients, img):
        self.name = name
        self.price = price
        self.stars = stars
        self.ingredients = ingredients
        self.img = img


Restaurantss = [Restaurante("Restaurant 1", "Incredible", "../static/main/images/menu.png"),
               Restaurante("Restaurant 2", "The best italian", "../static/main/images/menu.png"),
               Restaurante("Restaurant 3", "A simple restaurant", "../static/main/images/menu.png"),
               Restaurante("Restaurant 4", "Another interesting description", "../static/main/images/menu.png")]

Dishes = [Dish("Macarrones con bacon", 5.50, 4, ["Macarrones", "Bacon", "Tomate"], "../static/main/images/menu.png"),
          Dish("Cocido madrileño", 8.75, 4.5, ["Chorizo", "Tomate", "Morcilla", "Longaniza",
                                               "Chorizo", "Tomate", "Morcilla", "Longaniza", "Chorizo", "Tomate",
                                               "Morcilla", "Longaniza", "Chorizo", "Tomate", "Morcilla", "Longaniza"],
               "../static/main/images/menu.png"),
          Dish("Sopa", 4.40, 2, ["Caldo", "Pasta", "Avecren"], "../static/main/images/menu.png"),
          Dish("Macarrones con queso", 5.60, 4.3, ["Macarrones", "Queso", "Tomate"], "../static/main/images/menu.png")]


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def search(request):
    res = Restaurant.objects.all()
    return render(request, "main/search.html", {
        "restaurants": res
    })


def restaurant(request):
    return render(request, "main/restaurant.html", {
        "dishes": Dishes
    })


def restaurant_info(request):
    return render(request, "main/restaurant-info.html")


def filters(request):
    return render(request, "main/layout-filters.html")
