from django.shortcuts import render, redirect, get_object_or_404
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


def edit_reservation(request, pk):
    """
    Updates the specified reservation with new details input by the user.
    """

    if request.user.is_authenticated:
        res_instance = get_object_or_404(Reservation, id=pk)
        edit_form = ReservationForm(instance=res_instance)
    else:
        messages.warning(
            request,
            ("You cannot view this page without logging in.")
            )
        return redirect('home')

    if request.user == res_instance.user:
        if request.method == 'POST':
            edit_form = ReservationForm(request.POST, instance=res_instance)

            if edit_form.is_valid():

                edit_data = edit_form.save(commit=False)

                if Reservation.objects.filter(
                    user=edit_data.user,
                    date=edit_data.date,
                    time=edit_data.time,
                    no_of_people=edit_data.no_of_people,
                ).exists():
                    print('no change')
                else:
                    edit_data.save()
                    print('valid')

    context = {
        'form': edit_form,
    }
    return render(request, "reserve.html", context)