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
    Tests the views for the reservations app
    """

    def setUp(self):

        self.user = User.objects.create_user(
            username="Tony",
            password="password",
            email="admin@example.com",
            first_name="Tony",
            last_name="Guimaraes",
        )

        self.user2 = User.objects.create_user(
            username="tester", password="password1", email="test@example.com"
        )

        self.reservation = Reservation.objects.create(
            user=self.user,
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            email=self.user.email,
            date='2023-11-11',
            time='10:00:00',
            no_of_people='2',
        )

        past_reservation = Reservation.objects.create(
            user=self.user,
            date='2022-11-11',
            time='10:00:00',
            no_of_people='2',
        )

    def test_unauthorized_user_make_reservation_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        when they try access reservation page
        """

        response = self.client.get("/reservations/reserve/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Please login/signup as a customer '
                        'to make a reservation'
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
        }

        response = self.client.post('/reservations/reserve/', form)

        self.assertEqual(response.status_code, 200)

        url = reverse("reserve")
        self.assertEquals(resolve(url).func, make_reservation)
        self.assertTemplateUsed(response, "reservation_success.html")

    def test_double_booked_response(self):
        """
        Tests if functionality to prevent double bookings
        works correctly
        """

        self.client.force_login(self.user)

        form = {
            'date': '2023-11-11',
            'time': '10:00:00',
            'no_of_people': '2',
        }

        response = self.client.post('/reservations/reserve/', form)

        self.assertEqual(response.status_code, 200)

        url = reverse("reserve")
        self.assertEquals(resolve(url).func, make_reservation)
        self.assertTemplateUsed(response, "double_booked.html")

    def test_unauthorized_user_edit_reservation_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        when they try access the edit reservation page
        """

        response = self.client.get("/reservations/edit_reservation/1/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_edit_reservation(self):
        """
        Tests if functionality to edit a reservation
        works for logged in users
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

    def test_unauthorized_user_edit_response(self):
        """
        Tests if the correct response is given if a user tries to edit
        another users reservations
        """
        self.client.force_login(self.user2)
        response = self.client.get("/reservations/edit_reservation/1/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_edit_reservation_past_date_response(self):
        """
        Tests if the correct response is given when a user tries to edit
        a reservation for a past date
        """

        self.client.force_login(self.user)
        response = self.client.get("/reservations/edit_reservation/2/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You cannot edit a reservation for a past date'
                        )
        self.assertEqual(response.status_code, 302)

    def test_reservation_already_exists_edit_response(self):
        """
        Tests functionality for when a user submits an edit form
        with details that already exist
        """

        self.client.force_login(self.user)
        form = {
            'user': 'test',
            'first_name': 'Tony',
            'last_name': 'Guimaraes',
            'email': 'admin@example.com',
            'date': '2023-11-11',
            'time': '10:00:00',
            'no_of_people': '2',
        }

        response = self.client.post('/reservations/edit_reservation/1/', form)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Reservation details already exist'
                        )
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_user_delete_reservation_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        when they try access the delete reservation page
        """

        response = self.client.get('/reservations/delete_reservation/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_delete_reservation(self):
        """
        Tests if delete reservation functionality works correctly
        for logged in users for both past and future dates
        """

        self.client.force_login(self.user)
        response = self.client.get("/reservations/delete_reservation/1/")
        response = self.client.get("/reservations/delete_reservation/2/")
        self.assertEqual(response.status_code, 200)

        url = reverse("delete_reservation", args=[1])
        self.assertEquals(resolve(url).func, delete_reservation)
        self.assertTemplateUsed(response, "delete_reservation.html")

        response = self.client.post('/reservations/delete_reservation/1/')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'The reservation has been removed'
                        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.all().count(), 1)

    def test_unauthorized_user_delete_response(self):
        """
        Tests if the correct response is given if a user tries to delete
        another users reservation
        """
        self.client.force_login(self.user2)
        response = self.client.get("/reservations/delete_reservation/1/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)


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
            )

    def test_status_value_defaults_to_pending(self):
        """
        Tests that the reservation value for status defaults to pending
        """

        self.assertEqual(self.reservation.status, 'pending')

    def test_model_returns_first_name_string(self):
        """
        Tests if the model returns the first_name of the reservation
        as a string
        """

        self.assertEquals(str(self.reservation), 'Tony')

    def test_is_past_date_method_returns_correct_boolean(self):
        """
        Tests if the is_past_date method of the reservation
        model returns the correct boolean value
        """

        self.reservation.date = date.today() - timedelta(days=1)
        self.assertTrue(self.reservation.is_past_date)

    def test_is_past_time_method_returns_correct_boolean(self):
        """
        Tests if the is_past_date method of the reservation
        model returns the correct boolean value
        """

        self.reservation.date = '2023-03-23 09:00:00'
        self.assertTrue(self.reservation.is_past_time)
