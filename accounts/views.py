from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from reservations.models import Reservation
from .forms import EditUserForm


def home_page(request):
    """
    Renders the home page
    """
    return render(request, "index.html")


def profile_page(request):
    """
    Renders a profile page with details specific to the user
    """

    if request.user.is_authenticated and request.user.is_staff is False:
        f_name = request.user.first_name
        l_name = request.user.last_name
        username = request.user.username
        email_address = request.user.email

        reservations = Reservation.objects.filter(user=request.user)

        context = {
            'f_name': f_name,
            'l_name': l_name,
            'username': username,
            'email_address': email_address,
            'reservations': reservations,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('home')


def edit_account(request, pk):
    """
    Handles the editing of the specified user
    """

    user_instance = get_object_or_404(User, id=pk)

    if request.user == user_instance and request.user.is_staff is False:
        form = EditUserForm(instance=user_instance)

        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user_instance)
            if form.is_valid():
                form.save()
                messages.success(request, ("Account updated successfully"))
                return redirect('profile_page')
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('profile_page')

    context = {
        'form': form
    }
    return render(request, "edit_account.html", context)


def delete_account(request, pk):
    """
    Handles the deletion of a specified user
    """

    user_instance = get_object_or_404(User, id=pk)
    if request.user == user_instance and request.user.is_staff is False:
        if request.method == 'POST':
            user_instance.delete()
            messages.success(request, ("Your account has been deleted"))
            return redirect('home')
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('profile_page')

    context = {
        'user_instance': user_instance
    }
    return render(request, 'delete_account.html', context)
