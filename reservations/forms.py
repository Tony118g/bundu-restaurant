from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = (
            'date',
            'time',
            'no_of_people',
            'phone_number',
        )
