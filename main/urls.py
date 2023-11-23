from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("",
         views.index, name="index"),
    path("search/loc=<str:locationEntry>+food_filters=<str:celEntry>,<str:vegetEntry>,<str:veganEntry>,"
         "<str:nutsEntry>,<str:lactoseEntry>+price=<str:priceEntry>",
         views.search, name="search"),
    path("restaurant/<int:user_id>+food_filters=<str:celEntry>,<str:vegEntry>,<str:veganEntry>,"
         "<str:nutsEntry>,<str:lactoseEntry>+price=<str:priceEntry>",
         views.restaurant, name="restaurant"),
    path("restaurant/<int:user_id>/info/",
         views.restaurant_info, name="restaurant-info"),
    path("menu/<str:rest>/<str:menuid>",
         views.menu, name="menu")
]
