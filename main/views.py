from django.shortcuts import render


class Restaurante:
  def __init__(self, name):
    self.name = name


Restaurantes = [Restaurante("Restaurante 1"),
                Restaurante("Restaurante 2"),
                Restaurante("Restaurante 3"),
                Restaurante("Restaurante 4")]


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def search(request):
    return render(request, "main/search.html", {
        "restaurants": Restaurantes
    })
