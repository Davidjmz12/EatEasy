from django.shortcuts import render


# All the information for one restaurant
class Restaurant:
    def __init__(self, name, description, img):
        self.name = name
        self.description = description
        self.img = img


Restaurants = [Restaurant("Restaurant 1", "Incredible", "../static/main/images/menu.png"),
               Restaurant("Restaurant 2", "The best italian", "../static/main/images/menu.png"),
               Restaurant("Restaurant 3", "A simple restaurant", "../static/main/images/menu.png"),
               Restaurant("Restaurant 4", "Another interesting description", "../static/main/images/menu.png")]


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def search(request):
    return render(request, "main/search.html", {
        "restaurants": Restaurants
    })


def restaurant(request):
    return render(request, "main/restaurant.html")
