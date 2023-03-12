from . import views
from django.urls import path

urlpatterns = [
    path('reservations/reserve/', views.make_reservation, name='reserve'),
]
