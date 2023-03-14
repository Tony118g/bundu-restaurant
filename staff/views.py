from django.shortcuts import render, redirect


def staff_dashboard(request):

    if request.user.is_staff:
        return render(request, "dashboard.html")
    else:
        return redirect('home')
