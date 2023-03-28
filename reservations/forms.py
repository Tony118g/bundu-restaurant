from django import forms
from .models import Reservation
from datetime import date, datetime, timedelta

TOMORROW = date.today() + timedelta(days=1)


class ReservationForm(forms.ModelForm):
    """
    The form used to create a reservation request
    """

    date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date', 'min': TOMORROW}
        ))

    class Meta:
        model = Reservation
        fields = (
            'date',
            'time',
            'no_of_people',
        )
