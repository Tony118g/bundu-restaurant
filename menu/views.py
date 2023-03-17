from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import MenuItemForm


def add_menu_item(request):

    form = MenuItemForm()
    if request.user.is_staff:
        if request.method == 'POST':
            form = MenuItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('staff_dashboard')
    else:
        return redirect('home')

    context = {'form': form}
    return render(request, "add_item.html", context)
