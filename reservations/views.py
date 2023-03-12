from django.shortcuts import render, redirect
from reservations.models import Reservation
from django.contrib import messages
from .forms import ReservationForm


def make_reservation(request):

    if request.user.is_authenticated:
        reservation_form = ReservationForm()
        context = {
            "form": reservation_form,
        }
    else:
        messages.info(
            request,
            ("Please login/signup if you would like to make a reservation")
            )
        return redirect('account_login')

    if request.method == 'POST':

        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.instance.user = request.user
            reservation_form.instance.first_name = request.user.first_name
            reservation_form.instance.last_name = request.user.last_name

            form_data = reservation_form.save(commit=False)

            if Reservation.objects.filter(
                user=form_data.user,
                date=form_data.date,
                time=form_data.time,
            ).exists():
                return render(request, 'double_booked.html')
            else:
                form_data.save()
                return render(request, 'reservation_success.html')

    return render(request, 'reserve.html', context)
