from django.shortcuts import render


def home_page(request):
    return render(request, "index.html")


def profile_page(request):

    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, "index.html")
