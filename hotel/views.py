import datetime
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Room, Guest, Booking
from .forms import BookingCreateForm

# Create your views here.
def home(request):
    return render(request, 'hotel/home.html')

class RoomList(ListView):
    model = Room

class GuestList(ListView):
    model = Guest

class BookingCreate(CreateView):
    model=Booking
    template_name = 'hotel/booking_create_form.html'
    form_class = BookingCreateForm
    success_url = '/room/list'

    def form_valid(self, form):
        form.instance.start = datetime.date.today()
        form.instance.calc_stay()
        form.instance.calc_price()
        form.instance.book_room()
        return super().form_valid(form)