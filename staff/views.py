from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def staff_dashboard(request):

    if request.user.is_staff:
        user_count = User.objects.filter(
            is_superuser=False, is_staff=False
            ).count()
        context = {'user_count': user_count}
        return render(request, "dashboard.html", context)
    else:
        return redirect('home')
