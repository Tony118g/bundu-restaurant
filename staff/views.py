from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from reservations.models import Reservation


def staff_dashboard(request):

    if request.user.is_staff:
        user_count = User.objects.filter(
            is_superuser=False, is_staff=False
            ).count()
        context = {'user_count': user_count}
        return render(request, "dashboard.html", context)
    else:
        return redirect('home')


def pending_reservations(request):

    if request.user.is_staff:
        pending_list = Reservation.objects.filter(
                                                acknowledged=False
                                                ).order_by('date_of_request')
        
        context = {'pending_list': pending_list}
        return render(request, 'pending_reservations.html', context)
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('home')
