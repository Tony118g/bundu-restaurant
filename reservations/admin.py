from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class BookingAdmin(admin.ModelAdmin):
    """
    The class used to display reservations in admin panel
    """
    list_filter = (
        'user',
        'date',
        'status',
        )
    list_display = (
        'date',
        'time',
        'user',
        'no_of_people',
        'status',
        )
