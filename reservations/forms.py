from django import forms
from .models import Reservation
from datetime import date, datetime, timedelta

tomorrow = date.today() + timedelta(days=1)


class ReservationForm(forms.ModelForm):

    date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date', 'min': tomorrow}
        ))

    class Meta:
        model = Reservation
        fields = (
            'date',
            'time',
            'no_of_people',
        )
