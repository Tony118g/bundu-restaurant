from django.http import HttpRequest
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm
from django.urls import reverse, resolve
from django.contrib.messages import get_messages
from datetime import date, timedelta
from .views import (
    make_reservation,
    edit_reservation,
    delete_reservation,
)


class TestReservationViews(TestCase):
    """
    Tests the views for the reservations app.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="password", email="admin@example.com"
        )

        reservation = Reservation.objects.create(
            user=self.user,
            date='2023-11-11',
            time='10:00:00',
            no_of_people='2',
        )

    def test_user_logged_out_make_reservation(self):
        """
        Test unauthorized users are redirected
        when they try access reservation page
        """

        response = self.client.get("/reservations/reserve/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Please login/signup if you would '
                        'like to make a reservation'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_make_reservation(self):
        """
        Test functionality to make a reservation
        works correctly for logged in users
        """

        self.client.force_login(self.user)
        response = self.client.get("/reservations/reserve/")
        self.assertEqual(response.status_code, 200)

        url = reverse("reserve")
        self.assertEquals(resolve(url).func, make_reservation)
        self.assertTemplateUsed(response, "reserve.html")

        form = {
            'date': '2023-05-10',
            'time': '10:00:00',
            'no_of_people': '2',
            'phone_number': '07456789342',
        }

        response = self.client.post('/reservations/reserve/', form)

        self.assertEqual(response.status_code, 200)

        url = reverse("reserve")
        self.assertEquals(resolve(url).func, make_reservation)
        self.assertTemplateUsed(response, "reservation_success.html")

    def test_double_booked_response(self):
        """
        Test functionality to prevent double bookings
        works correctly
        """

        self.client.force_login(self.user)

        form = {
            'date': '2023-11-11',
            'time': '10:00:00',
            'no_of_people': '2',
            'phone_number': '07456789342',
        }

        response = self.client.post('/reservations/reserve/', form)

        self.assertEqual(response.status_code, 200)

        url = reverse("reserve")
        self.assertEquals(resolve(url).func, make_reservation)
        self.assertTemplateUsed(response, "double_booked.html")

    def test_user_logged_out_edit_reservation(self):
        """
        Test unauthorized users are redirected
        when they try access edit reservation page
        """

        response = self.client.get("/reservations/edit_reservation/1/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You cannot view this page without logging in.'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_edit_reservation(self):
        """
        Test functionality to edit a reservation
        works for logged in user
        """
        self.client.force_login(self.user)
        response = self.client.get("/reservations/edit_reservation/1/")
        self.assertEqual(response.status_code, 200)

        url = reverse("edit_reservation", args=[1])
        self.assertEquals(resolve(url).func, edit_reservation)
        self.assertTemplateUsed(response, "reserve.html")

        form = {
            'date': '2023-05-10',
            'time': '10:00:00',
            'no_of_people': '2',
        }

        response = self.client.post('/reservations/edit_reservation/1/', form)

        self.assertEqual(response.status_code, 200)

        url = reverse("reserve")
        self.assertEquals(resolve(url).func, make_reservation)
        self.assertTemplateUsed(response, "reservation_success.html")

    def test_no_changes_edit_response(self):
        """
        Test functionality for when user submits an edit form
        without any changes
        """

        self.client.force_login(self.user)

        form = {
            'date': '2023-11-11',
            'time': '10:00:00',
            'no_of_people': '2',
            'phone_number': '07456789342',
        }

        response = self.client.post('/reservations/edit_reservation/1/', form)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'No changes have been made'
                        )
        self.assertEqual(response.status_code, 200)

    def test_user_logged_out_delete_reservation(self):
        """
        Test unauthorized users are redirected when
        they try access the delete reservation page
        """

        response = self.client.get('/reservations/delete_reservation/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You cannot view this page without logging in.'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_delete_reservation(self):
        """
        Test delete reservation functionality works correctly
        for logged in users
        """

        self.client.force_login(self.user)
        response = self.client.get("/reservations/delete_reservation/1/")
        self.assertEqual(response.status_code, 200)

        url = reverse("delete_reservation", args=[1])
        self.assertEquals(resolve(url).func, delete_reservation)
        self.assertTemplateUsed(response, "delete_reservation.html")

        response = self.client.post('/reservations/delete_reservation/1/')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'The reservation has been cancelled'
                        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.all().count(), 0)


class TestReservationModels(TestCase):
    """
    Tests the reservations models
    """

    def setUp(self):

        self.user = User.objects.create_user(
            username="test", password="password", email="admin@example.com"
        )

        self.reservation = Reservation.objects.create(
            user=self.user,
            first_name='Tony',
            last_name='Gum',
            no_of_people=4,
            email='test_@gmail.com',
            date='2023-11-12',
            time='12:00:00',
            phone_number='+263 78 050 8241'
            )

    def test_status_values_default_to_false(self):
        """
        Tests that reservation values for approved, denied
        and acknowledged field default to false
        """

        self.assertEqual(self.reservation.approved, False)
        self.assertEqual(self.reservation.denied, False)
        self.assertEqual(self.reservation.acknowledged, False)

    def test_model_returns_first_name_string(self):
        """
        Tests if the model returns the first_name of reservation
        as a string
        """

        self.assertEquals(str(self.reservation), 'Tony')

    def test_is_past_date_method_returns_correct_boolean(self):
        """
        Tests if the is_past_date method of reservation model
        returns the correct boolean field
        """

        self.reservation.date = date.today() - timedelta(days=1)
        self.assertTrue(self.reservation.is_past_date)
