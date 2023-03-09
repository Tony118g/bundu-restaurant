from django.shortcuts import render, redirect


def home_page(request):
    return render(request, "index.html")


def profile_page(request):

    if request.user.is_authenticated:
        f_name = request.user.first_name
        l_name = request.user.last_name
        username = request.user.username
        email_address = request.user.email

        context = {
            'f_name': f_name,
            'l_name': l_name,
            'username': username,
            'email_address': email_address,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('home')
