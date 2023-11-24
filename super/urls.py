from django.urls import path

from . import views

app_name = "super"
urlpatterns = [
    path("", views.index, name="index"),
    path("management", views.management, name="management"),
    path("deleteRes/<int:pk>", views.deleteRes, name="deleteRes"),
    path("management/<int:pk>", views.oneRestaurant, name="oneRes"),
    path("management/notificate/<int:pk>", views.notification, name="notification"),
    path("management/ingredients", views.ingredients, name="ingredients"),
    path("management/ingredients/add", views.addIng, name="addIng"),
    path("statistic_price/", views.statistic_price, name="statistic_price"),
    path("statistic_filter/", views.statistic_filter, name="statistic_filter"),
    path("statistic_city/", views.statistic_city, name="statistic_city")
]
