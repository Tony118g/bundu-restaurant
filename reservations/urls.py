from . import views
from django.urls import path

urlpatterns = [
    path('reservations/reserve/', views.make_reservation, name='reserve'),
    path(
        'reservations/edit_reservation/<str:pk>/',
        views.edit_reservation,
        name='edit_reservation'
        ),
    path(
        'reservations/delete_reservation/<str:pk>/',
        views.delete_reservation,
        name='delete_reservation'
        ),
]
