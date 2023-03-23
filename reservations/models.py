from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


STATUS = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('denied', 'denied'),
    )


no_of_people_choices = (
    (1, "1 person"),
    (2, "2 people"),
    (3, "3 people"),
    (4, "4 people"),
    (5, "5 people"),
    (6, "6 people"),
    )

reservation_times = (
    (datetime.strptime("0800", "%H%M").time(), "0800"),
    (datetime.strptime("0900", "%H%M").time(), "0900"),
    (datetime.strptime("1000", "%H%M").time(), "1000"),
    (datetime.strptime("1100", "%H%M").time(), "1100"),
    (datetime.strptime("1200", "%H%M").time(), "1200"),
    (datetime.strptime("1300", "%H%M").time(), "1300"),
    (datetime.strptime("1400", "%H%M").time(), "1400"),
    (datetime.strptime("1500", "%H%M").time(), "1500"),
    (datetime.strptime("1600", "%H%M").time(), "1600"),
    (datetime.strptime("1700", "%H%M").time(), "1700"),
    (datetime.strptime("1800", "%H%M").time(), "1800"),
    (datetime.strptime("1900", "%H%M").time(), "1900"),
    (datetime.strptime("2000", "%H%M").time(), "2000"),
    )


class Reservation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35, null=False, blank=False)
    last_name = models.CharField(max_length=35, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    no_of_people = models.IntegerField(choices=no_of_people_choices, default=1)
    date = models.DateField()
    time = models.TimeField(choices=reservation_times)
    date_of_request = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS, default="pending")

    def __str__(self):
        return self.first_name

    @property
    def is_past_date(self):
        """
        Returns True if the reservation date is either past or present
        """
        return date.today() >= self.date

    @property
    def is_past_time(self):
        """
        Returns True if the reservation time is past or present
        """
        res_date_time = (str(self.date), str(self.time))
        crrnt_dte_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return crrnt_dte_str >= ' '.join(res_date_time)
