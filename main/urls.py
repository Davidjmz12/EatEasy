from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/loc=<str:location>", views.search, name="search"),
    path("restaurant/<int:user_id>/food_filt=<int:cel>,<int:veg>,<int:vegan>", views.restaurant, name="restaurant"),
    path("restaurant/<int:user_id>/info/", views.restaurant_info, name="restaurant-info"),
    path("menu/<str:rest>/<str:menuid>", views.menu, name="menu")
]
