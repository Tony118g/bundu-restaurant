from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from reservations.models import Reservation
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date, datetime


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
        messages.warning(
            request, ('You are not authorized to view this page')
            )
        return redirect('home')


def reservation_list(request, status):
    """
    Renders a page to display reservations
    pertaining to the status provided
    """

    if request.user.is_staff:
        if status == 'pending':
            pending_list = Reservation.objects.filter(
                                                    status='pending'
                                                    ).order_by(
                                                        'date_of_request'
                                                        )
            for reservation in pending_list:
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                res_datetime = ' '.join(
                    (str(reservation.date), str(reservation.time))
                    )
                if current_datetime >= res_datetime:
                    reservation.status = 'denied'
                    reservation.save()

                    context = {'reservation': reservation}
                    email_template = render_to_string(
                        'expired_feedback_email.html', context
                        )
                    send_mail(
                        'Bundu Restaurant expired reservation feedback',
                        email_template,
                        settings.EMAIL_HOST_USER,
                        [reservation.email],
                        fail_silently=False
                    )

            reservation_list = Reservation.objects.filter(
                                                    status='pending'
                                                    ).order_by(
                                                        'date_of_request'
                                                        )
        elif status == 'approved':
            reservation_list = Reservation.objects.filter(
                                                    status='approved'
                                                    ).order_by('-date')
        elif status == 'denied':
            reservation_list = Reservation.objects.filter(
                                                    status='denied'
                                                    ).order_by('-date')

        context = {
            'reservation_list': reservation_list,
            'status': status,
            }
        return render(request, 'reservations_list.html', context)
    else:
        messages.warning(request, ('You are not authorized to view this page'))
        return redirect('home')


def approve_reservation(request, pk):
    """
    Sets status to approved and sends an approval email
    """

    next = request.POST.get('next', '/')
    try:
        reservation = Reservation.objects.get(id=pk)
    except Reservation.DoesNotExist:
        messages.warning(request, ('This reservation no longer exists'))
        return redirect(next)

    if request.user.is_staff:
        reservation.status = 'approved'

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
        messages.success(request, ('Reservation has been approved'))
        return redirect(next)
    else:
        messages.warning(request, ('You are not authorized to view this page'))
        return redirect('home')


def deny_reservation(request, pk):
    """
    Sets status to denied for the specified reservation
    """

    next = request.POST.get('next', '/')
    try:
        reservation = Reservation.objects.get(id=pk)
    except Reservation.DoesNotExist:
        messages.warning(request, ('This reservation no longer exists'))
        return redirect(next)

    print(reservation)

    if request.user.is_staff:
        reservation.status = 'denied'
        reservation.save()

        context = {'reservation': reservation}

        email_template = render_to_string('denied_email.html', context)
        send_mail(
            "Bundu Restaurant reservation denied",
            email_template,
            settings.EMAIL_HOST_USER,
            [reservation.email],
            fail_silently=False
        )
        messages.success(request, ('Reservation has been denied'))
        return redirect(next)
    else:
        messages.warning(request, ('You are not authorized to view this page'))
        return redirect('home')


def current_date_reservations(request):
    """
    Gets the approved reservations for the current date for staff to view
    """
    if request.user.is_staff:
        today_res_list = Reservation.objects.filter(
            date=date.today(), status='approved'
            )

        context = {'today_res_list': today_res_list}

        return render(request, 'current_reservations.html', context)
    else:
        messages.warning(request, ('You are not authorized to view this page'))
        return redirect('home')


def search_date(request):
    """
    Gets reservations for the date provided
    """
    date = request.GET['date']
    search_results = Reservation.objects.filter(date=date, status='approved')

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
        full_name = ' '.join(
                    (str(reservation.first_name), str(reservation.last_name))
                    )
        if search_name.casefold() in full_name:
            search_results.append(reservation)

    context = {'search_results': search_results}
    return render(request, 'name_search_results.html', context)
