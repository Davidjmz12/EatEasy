from django.urls import path

from . import views

app_name = "super"
urlpatterns = [
    path("", views.index, name="index"),
]
