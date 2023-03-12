from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class BookingAdmin(admin.ModelAdmin):
    """
    The class used to display reservations in admin panel
    """
    list_filter = (
        'user',
        'approved',
        'denied',
        'acknowledged',
        'date'
        )
    list_display = (
        'id',
        'user',
        'date',
        'time',
        'no_of_people',
        'approved',
        'denied',
        'acknowledged'
        )
