from django import forms
from .models import Booking


class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('room', 'guest', 'length_of_stay')  # start is today()
