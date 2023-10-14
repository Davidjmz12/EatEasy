from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("restaurant/info/", views.restaurant_info, name="restaurant-info"),
    path("prueba/", views.filters, name="filters")
]
