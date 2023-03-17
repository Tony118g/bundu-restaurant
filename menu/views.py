from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem
from .forms import MenuItemForm


def add_menu_item(request):

    if request.user.is_staff:
        form = MenuItemForm()
        if request.method == 'POST':
            form = MenuItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                if form.instance.status == 1:
                    messages.success(
                        request,
                        ("Menu item successfully published.")
                        )
                else:
                    messages.success(
                        request,
                        ("Menu draft saved as draft.")
                        )
                return redirect('staff_dashboard')
        else:
            context = {'form': form}
            return render(request, "add_item.html", context)
    else:
        messages.warning(
            request,
            ("Only logged in staff members can view this page")
            )
        return redirect('home')
