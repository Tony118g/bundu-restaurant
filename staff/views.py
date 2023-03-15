from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.conf import settings
from reservations.models import Reservation
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date


def staff_dashboard(request):
    """
    Renders the staff dashboard if the user is staff
    """

    if request.user.is_staff:
        user_count = User.objects.filter(
            is_superuser=False, is_staff=False
            ).count()
        context = {'user_count': user_count}
        return render(request, "dashboard.html", context)
    else:
        return redirect('home')


def reservation_list(request, status):
    """
    Renders a page to display reservations
    pertaining to the status provided
    """

    if request.user.is_staff:
        if status == 'pending':
            reservation_list = Reservation.objects.filter(
                                                    acknowledged=False
                                                    ).order_by(
                                                        'date_of_request'
                                                        )
        elif status == 'approved':
            reservation_list = Reservation.objects.filter(
                                                    approved=True
                                                    ).order_by('date')
        elif status == 'denied':
            reservation_list = Reservation.objects.filter(
                                                    denied=True
                                                    ).order_by('date')

        context = {
            'reservation_list': reservation_list,
            'status': status,
            }
        return render(request, 'reservations_list.html', context)
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('home')


def approve_reservation(request, pk):
    """
    Sets approved and acknowledged fields to true for specified reservation
    """

    reservation = get_object_or_404(Reservation, id=pk)

    if request.user.is_staff:
        next = request.POST.get('next')
        reservation.approved = True
        reservation.acknowledged = True
        reservation.save()

        context = {'reservation': reservation}

        email_template = render_to_string('approved_email.html', context)
        send_mail(
            "Bundu Restaurant reservation approved",
            email_template,
            settings.EMAIL_HOST_USER,
            [reservation.email],
            fail_silently=False
        )

        return redirect(next)
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('home')


def deny_reservation(request, pk):
    """
    Sets denied and acknowledged fields to true for specified reservation
    """

    reservation = get_object_or_404(Reservation, id=pk)

    if request.user.is_staff:
        next = request.POST.get('next')
        reservation.denied = True
        reservation.acknowledged = True
        reservation.save()
        return redirect(next)
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('home')


def current_date_reservations(request):
    """
    Gets the approved reservations for the current date for staff to view
    """

    today_res_list = Reservation.objects.filter(
        date=date.today(), approved=True
        )

    context = {'today_res_list': today_res_list}

    return render(request, 'current_reservations.html', context)


def search_date(request):
    """
    Gets reservations for the date provided
    """
    date = request.GET['date']
    search_results = Reservation.objects.filter(date=date, approved=True)

    context = {'search_results': search_results}
    return render(request, 'date_search_results.html', context)


def search_name(request):
    """
    Gets reservations for the name provided
    """
    search_name = request.GET['name']

    all_reservations = Reservation.objects.all()

    search_results = []
    for reservation in all_reservations:
        full_name = reservation.user.get_full_name()
        if search_name in full_name:
            search_results.append(reservation)

    context = {'search_results': search_results}
    return render(request, 'name_search_results.html', context)
