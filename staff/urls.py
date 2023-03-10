from . import views
from django.urls import path

urlpatterns = [
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path(
        'staff/reservations/<status>/',
        views.reservation_list, name='reservation_list'
        ),
    path(
        'staff/approve_reservation/<str:pk>/',
        views.approve_reservation, name='approve_reservation'
        ),
    path(
        'staff/deny_reservation/<str:pk>/',
        views.deny_reservation, name='deny_reservation'
        ),
]
