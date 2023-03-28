from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import Reservation
from django.contrib import messages
from .forms import ReservationForm
from datetime import date


def make_reservation(request):
    """
    Handles the creation of reservation requests by users
    """

    if request.user.is_authenticated and request.user.is_staff is False:
        heading = 'Make a reservation'
        reservation_form = ReservationForm()

        context = {
            'heading': heading,
            'form': reservation_form,
        }
    else:
        messages.info(
            request,
            ("Please login/signup as a customer to make a reservation")
            )
        return redirect('account_login')

    if request.method == 'POST':

        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.instance.user = request.user
            reservation_form.instance.first_name = request.user.first_name
            reservation_form.instance.last_name = request.user.last_name
            reservation_form.instance.email = request.user.email

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
    Handles the editing of the specified reservation
    using new details input by the user.
    """
    res_instance = get_object_or_404(Reservation, id=pk)

    if request.user == res_instance.user:

        if request.method == 'POST':
            edit_form = ReservationForm(request.POST, instance=res_instance)

            if edit_form.is_valid():
                edit_form.instance.first_name = request.user.first_name
                edit_form.instance.last_name = request.user.last_name
                edit_form.instance.email = request.user.email

                edit_data = edit_form.save(commit=False)

                if Reservation.objects.filter(
                    user=edit_data.user,
                    first_name=edit_data.first_name,
                    last_name=edit_data.last_name,
                    email=edit_data.email,
                    date=edit_data.date,
                    time=edit_data.time,
                    no_of_people=edit_data.no_of_people,
                ).exists():
                    messages.info(request, 'Reservation details already exist')
                else:
                    res_instance.status = 'pending'
                    edit_data.save()
                    return render(request, 'reservation_success.html')

        if res_instance.date > date.today():
            edit_form = ReservationForm(instance=res_instance)
            editing = True
            heading = 'Edit your reservation below'

            context = {
                'form': edit_form,
                'heading': heading,
                'editing': editing,
            }
            return render(request, "reserve.html", context)
        else:
            messages.warning(
                request,
                ('You cannot edit a reservation for a past date')
                )
            return redirect('profile_page')

    else:
        messages.warning(
            request,
            ('You are not authorized to view this page')
            )
        return redirect('home')


def delete_reservation(request, pk):
    """
    Handles deletion of the specified reservation
    """
    res_instance = get_object_or_404(Reservation, id=pk)

    if request.user == res_instance.user:

        if request.method == 'POST':
            res_instance.delete()
            messages.success(request, 'The reservation has been removed')
            return redirect('profile_page')

        if res_instance.is_past_date:
            action = 'delete record of'
        else:
            action = 'cancel'

        context = {
            'res_instance': res_instance,
            'action': action,
        }
        return render(request, 'delete_reservation.html', context)

    else:
        messages.warning(
            request,
            ('You are not authorized to view this page')
            )
        return redirect('home')
