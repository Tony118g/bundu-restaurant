from django.shortcuts import render


def make_reservation(request):
    return render(request, "reserve.html")
