from django.urls import path

from . import views

app_name = "super"
urlpatterns = [
    path("", views.index, name="index"),
    path("management", views.management, name="management"),
    path("deleteRes/<int:pk>", views.deleteRes, name="deleteRes"),
    path("management/<int:pk>", views.oneRestaurant, name="oneRes"),
    path("management/notificate/<int:pk>", views.notification, name="notification")
]
