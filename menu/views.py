from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import MenuItemForm


def add_menu_item(request):

    if request.user.is_staff:
        form = MenuItemForm()
        if request.method == 'POST':
            form = MenuItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('staff_dashboard')
        else:
            context = {'form': form}
            return render(request, "add_item.html", context)
    else:
        return redirect('home')
