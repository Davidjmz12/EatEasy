from django.urls import path

from . import views

app_name = "infouser"
urlpatterns = [
    path("", views.index, name="index"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("newmenu/", views.newMenu, name="newmenu"),
    path("client/", views.client,name="client"),
    path("update_info_client/", views.update_info_client,name="update_info_client"),
    path("changeinfo/", views.changeinfo, name="changeinfo"),
    path("update_info/", views.update_info, name="update_info"),
    path("menu/", views.menu, name="menu"),
    path("client/", views.client, name="client"),
    path("notifications/", views.notification, name="notifications"),
    path("notifications/<int:notification_id>", views.infoNotifications, name="infoNot"),
    path("notifications/read/<int:notification_id>", views.markAsRead, name="markAsRead"),
    path("notifications/delete/<int:notification_id>", views.deleteNotification, name="delNot"),
    path("menu/<str:menuid>/", views.menu, name="menu"),
    path("changemenu/<str:menuid>/", views.changemenu, name="changemenu"),
    path("changemenu/delete/<str:menuid>/", views.deleteMenu, name="deletemenu"),
    path("update_menu/<str:menuid>/", views.update_menu, name="update_menu"),
    path("statistics/<str:typeGraph>", views.statistics, name="statistics"),
    path("comments/delete/<int:user_pk>/<str:menuid>/<str:rest>", views.delete_comment, name="delCom")

]
