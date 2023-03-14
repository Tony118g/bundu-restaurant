from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from reservations.models import Reservation


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
