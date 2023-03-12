from django.shortcuts import render
from .forms import ReservationForm


def make_reservation(request):

    reservation_form = ReservationForm()
    context = {'form': reservation_form}

    return render(request, 'reserve.html', context)
