from django.urls import path

from . import views

app_name = "super"
urlpatterns = [
    path("", views.index, name="index"),
    path("management", views.management, name="management")
]
