from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import EditUserForm


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


def edit_account(request, pk):
    user_instance = get_object_or_404(User, id=pk)

    if request.user == user_instance:
        form = EditUserForm(instance=user_instance)

        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user_instance)
            if form.is_valid():
                form.save()
                messages.success(request, ("Account updated succesfully"))
                return redirect('profile_page')
    else:
        messages.warning(request, ("You are not authorized to view this page"))
        return redirect('profile_page')

    context = {
        'form': form
    }
    return render(request, "edit_account.html", context)

