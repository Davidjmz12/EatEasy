from django.shortcuts import render


class Restaurant:
    def __init__(self, name):
        self.name = name


Restaurants = [Restaurant("Restaurant 1"),
               Restaurant("Restaurant 2"),
               Restaurant("Restaurant 3"),
               Restaurant("Restaurant 4")]


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def search(request):
    return render(request, "main/search.html", {
        "restaurants": Restaurants
    })
