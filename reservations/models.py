from django.db import models
from django.contrib.auth.models import User


no_of_people_choices = (
    (1, "1 person"),
    (2, "2 people"),
    (3, "3 people"),
    (4, "4 people"),
    (5, "5 people"),
    (6, "6 people"),
    )

reservation_times = (
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    )


class Reservation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35, null=False, blank=False)
    last_name = models.CharField(max_length=35, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.IntegerField(blank=True, null=True)
    no_of_people = models.IntegerField(choices=no_of_people_choices, default=1)
    date = models.DateField()
    time = models.TimeField(choices=reservation_times)
    date_of_request = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    denied = models.BooleanField(default=False)
    acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
