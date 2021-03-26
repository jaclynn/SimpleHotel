from django.shortcuts import render
from django.views.generic import ListView
from .models import Room

# Create your views here.
def home(request):
    return render(request, 'hotel/home.html')

class RoomList(ListView):
    model = Room