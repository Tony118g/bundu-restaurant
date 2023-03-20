from django.shortcuts import render, redirect, get_object_or_404
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
    starter_items = MenuItem.objects.filter(status=1, category='starter')
    main_items = MenuItem.objects.filter(status=1, category='main')
    desert_items = MenuItem.objects.filter(status=1, category='desert')

    context = {
        'starter_items': starter_items,
        'main_items': main_items,
        'desert_items': desert_items,
        }
    return render(request, 'menu.html', context)


def menu_drafts(request):
    """
    Renders the menu drafts page
    """

    if request.user.is_staff:
        menu_drafts = MenuItem.objects.filter(status=0)
        context = {
            'menu_drafts': menu_drafts,
        }

        return render(request, 'menu_drafts.html', context)

    else:
        messages.warning(
            request,
            ("Only logged in staff members can view this page")
            )
        return redirect('home')


def edit_menu_item(request, pk):
    """
    Updates the specified menu item with the new details input by the user
    """

    item_instance = get_object_or_404(MenuItem, id=pk)

    if request.user.is_staff:
        form = MenuItemForm(instance=item_instance)

        if request.method == 'POST':
            form = MenuItemForm(
                request.POST, request.FILES, instance=item_instance
                )
            if form.is_valid():
                form.save()
                if form.instance.status == 1:
                    messages.success(
                        request,
                        ("Menu item has been edited and published.")
                        )
                else:
                    messages.success(
                        request,
                        ("Menu item saved as draft.")
                        )
                return redirect('staff_dashboard')

        context = {
            'form': form
        }
        return render(request, "add_item.html", context)

    else:
        messages.warning(
            request,
            ("Only logged in staff members can view this page")
            )
        return redirect('home')
