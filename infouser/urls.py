from django.urls import path

from . import views

app_name = "infouser"
urlpatterns = [
    path("", views.index, name="index"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("newmenu/", views.newMenu, name="newmenu"),
    path("news/", views.news, name="news"),
    path("client/", views.client, name="client"),
    path("notifications/", views.notification, name="notifications"),
    path("notifications/<int:notification_id>", views.infoNot, name="infoNot"),
    path("notifications/delete/<int:notification_id>", views.deleteNotification, name="delNot")
]
