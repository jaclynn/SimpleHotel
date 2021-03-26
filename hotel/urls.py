from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('room/list', views.RoomList.as_view(), name="roomlist"),
   path('guest/list', views.GuestList.as_view(), name="guestlist"),
   path('booking/create', views.BookingCreate.as_view(), name="bookingcreate"),

]