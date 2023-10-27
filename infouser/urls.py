from django.urls import path

from . import views

app_name = "infouser"
urlpatterns = [
    path("", views.index, name="index"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("newmenu/", views.newmenu, name="newmenu"),
    path("news/", views.news, name="news")
]
