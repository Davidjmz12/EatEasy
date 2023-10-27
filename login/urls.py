from django.urls import path

from . import views

app_name = "login"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("register/restaurant", views.registerRest, name="registerRestaurant"),
    path("register/user", views.registerUser, name="registerUser"),
]
