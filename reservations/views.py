from django.shortcuts import render, redirect
from reservations.models import Reservation
from .forms import ReservationForm


def make_reservation(request):

    if request.user.is_authenticated:
        reservation_form = ReservationForm()
        context = {
            "form": reservation_form,
        }
    else:
        return redirect('account_login')

    if request.method == 'POST':

        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.instance.user = request.user
            reservation_form.instance.first_name = request.user.first_name
            reservation_form.instance.last_name = request.user.last_name

            reservation_form.save()
            return redirect('home')

    return render(request, 'reserve.html', context)
