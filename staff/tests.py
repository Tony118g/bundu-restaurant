from django.test import TestCase
from django.contrib.auth.models import User
from reservations.models import Reservation
from django.urls import reverse, resolve
from django.contrib.messages import get_messages
from .views import (
    staff_dashboard,
    reservation_list,
    approve_reservation,
    deny_reservation,
    current_date_reservations,
    search_date,
    search_name,
)


class TestStaffViews(TestCase):
    """
    Tests the views for the staff app.
    """

    def setUp(self):

        self.user = User.objects.create_user(
            username="test", password="password", email="admin@example.com"
        )

        self.staff_user = User.objects.create_user(
            username="staff",
            password="staff_password",
            email="admin@example.com",
            is_staff=True
        )

        self.reservation = Reservation.objects.create(
            user=self.user,
            date='2023-11-11',
            time='10:00:00',
            no_of_people='2',
        )

    def test_staff_dashboard_render(self):
        """
        Tests if the dashboard page renders correctly
        for staff users
        """
        self.client.force_login(self.staff_user)
        response = self.client.get('/staff/dashboard/')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_dashboard')
        self.assertEquals(resolve(url).func, staff_dashboard)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_staff_dashboard_unauthorized_user_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        when they try access the dashboard page
        """
        self.client.force_login(self.user)
        response = self.client.get('/staff/dashboard/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_staff_reservations_list_render(self):
        """
        Tests if the reservations list page renders each
        reservation category correctly for staff users
        """
        self.client.force_login(self.staff_user)
        response = self.client.get('/staff/reservations/pending/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/staff/reservations/approved/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/staff/reservations/denied/')
        self.assertEqual(response.status_code, 200)

        url = reverse('reservation_list', args=['pending'])
        self.assertEquals(resolve(url).func, reservation_list)
        self.assertTemplateUsed(response, 'reservations_list.html')

        url = reverse('reservation_list', args=['approved'])
        self.assertEquals(resolve(url).func, reservation_list)
        self.assertTemplateUsed(response, 'reservations_list.html')

        url = reverse('reservation_list', args=['approved'])
        self.assertEquals(resolve(url).func, reservation_list)
        self.assertTemplateUsed(response, 'reservations_list.html')

    def test_staff_reservations_list_unauthorized_user_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        when they try access the staff reservations page
        """
        self.client.force_login(self.user)
        response = self.client.get('/staff/reservations/pending/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_staff_can_approve_reservations(self):
        """
        Tests if staff can approve reservations
        """
        self.client.force_login(self.staff_user)

        response = self.client.post('/staff/approve_reservation/1/')

        self.assertEqual(Reservation.objects.last().status, 'approved')
        self.assertEqual(response.status_code, 302)

        url = reverse('approve_reservation', args=[1])
        self.assertEquals(resolve(url).func, approve_reservation)

    def test_unauthorized_user_approve_reservation_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        if they try to approve a reservation via the url
        """
        self.client.force_login(self.user)

        response = self.client.post('/staff/approve_reservation/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_staff_can_deny_reservations(self):
        """
        Tests if staff can deny reservations
        """
        self.client.force_login(self.staff_user)

        response = self.client.post('/staff/deny_reservation/1/')

        self.assertEqual(Reservation.objects.last().status, 'denied')
        self.assertEqual(response.status_code, 302)

        url = reverse('deny_reservation', args=[1])
        self.assertEquals(resolve(url).func, deny_reservation)

    def test_unauthorized_user_deny_reservation_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        if they try to deny a reservation via the url
        """
        self.client.force_login(self.user)

        response = self.client.post('/staff/deny_reservation/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_staff_can_view_current_date_reservations(self):
        """
        Tests if the page showing reservations for the current date
        renders correctly for staff users
        """
        self.client.force_login(self.staff_user)
        response = self.client.get('/staff/current_reservations/')
        self.assertEqual(response.status_code, 200)

        url = reverse('current_reservations')
        self.assertEquals(resolve(url).func, current_date_reservations)
        self.assertTemplateUsed(response, 'current_reservations.html')

    def test_unauthorized_user_current_date_reservations_redirect(self):
        """
        Tests if unauthorized users are redirected with a message
        if they try to access the page for current date reservations
        """
        self.client.force_login(self.user)

        response = self.client.get('/staff/current_reservations/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_search_reservations_by_date(self):
        """
        Tests if functionality to search reservations
        by date works correctly
        """
        self.client.force_login(self.staff_user)
        search_dte = '2023-11-11'
        response = self.client.get('/staff/search_date/', {'date': search_dte})

        self.assertEqual(response.status_code, 200)

        url = reverse('search_date')
        self.assertEquals(resolve(url).func, search_date)
        self.assertTemplateUsed(response, 'date_search_results.html')

    def test_search_reservations_by_name(self):
        """
        Tests if functionality to search reservations
        by name works correctly
        """
        self.client.force_login(self.staff_user)
        search_nme = 'test'
        response = self.client.get('/staff/search_name/', {'name': search_nme})

        self.assertEqual(response.status_code, 200)

        url = reverse('search_name')
        self.assertEquals(resolve(url).func, search_name)
        self.assertTemplateUsed(response, 'name_search_results.html')

    def test_past_pending_reservations_automatically_denied(self):
        """
        Tests if pending reservations that have past are
        automatically denied when a staff member
        accesses the pending reservations page
        """
        past_reservation = Reservation.objects.create(
            user=self.user,
            date='2022-11-11',
            time='10:00:00',
            no_of_people='2',
        )
        self.assertEqual(Reservation.objects.last().status, 'pending')

        self.client.force_login(self.staff_user)
        response = self.client.get('/staff/reservations/pending/')
        self.assertEqual(Reservation.objects.last().status, 'denied')

    def test_deleted_reservation_staff_feedback(self):
        """
        Tests if the correct feedback is provided when a staff member
        has not refreshed the page and tries to approve or deny a
        reservation that has been deleted.
        """
        self.client.force_login(self.staff_user)

        self.reservation.delete()

        response = self.client.post('/staff/approve_reservation/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'This reservation no longer exists'
                        )
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/staff/deny_reservation/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'This reservation no longer exists'
                        )
        self.assertEqual(response.status_code, 302)
