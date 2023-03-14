from . import views
from django.urls import path

urlpatterns = [
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/pending/', views.pending_reservations, name='pending_reservations'),
]
