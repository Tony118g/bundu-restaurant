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


def menu_page(request):
    """
    Renders the menu page
    """
    starter_items = MenuItem.objects.filter(status=0, category='starter')
    main_items = MenuItem.objects.filter(status=0, category='main')
    desert_items = MenuItem.objects.filter(status=0, category='desert')

    context = {
        'starter_items': starter_items,
        'main_items': main_items,
        'desert_items': desert_items,
        }
    return render(request, 'menu.html', context)
