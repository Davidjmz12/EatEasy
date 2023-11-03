from django.urls import path

from . import views

app_name = "infouser"
urlpatterns = [
    path("", views.index, name="index"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("newmenu/", views.newMenu, name="newmenu"),
    path("news/", views.news, name="news"),
    path("client/", views.client,name="client"),
    path("changeinfo/", views.changeinfo, name="changeinfo"),
    path("update_info/", views.update_info, name="update_info"),
    path("menu/<str:menuid>/", views.menu, name="menu"),
    path("changemenu/<str:menuid>/", views.changemenu, name="changemenu"),
    path("update_menu/<str:menuid>/", views.update_menu, name="update_menu"),
]
