from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    """
    The class used to display menu items in the admin panel
    """
    list_filter = (
        'category',
        'available',
        'status'
        )
    list_display = (
        'title',
        'category',
        'available',
        'status'
        )
