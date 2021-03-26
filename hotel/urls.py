from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('room/list', views.RoomList.as_view(), name="roomlist"),

]