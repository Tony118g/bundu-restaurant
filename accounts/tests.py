from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.contrib.messages import get_messages
from accounts.views import (
    profile_page,
    edit_account,
    delete_account,
    home_page,
)


class TestViews(TestCase):
    """
    Tests the views for the accounts app.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="password", email="admin@example.com"
        )

    def test_home_page(self):
        """
        Test home page renders correctly
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        url = reverse("home")
        self.assertEquals(resolve(url).func, home_page)
        self.assertTemplateUsed(response, "index.html")

    def test_profile_page(self):
        """
        Test unauthorized users are redirected
        when they try access profile page
        """

        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_profile_page(self):
        """
        Test profile page renders correctly for logged in users
        """

        self.client.force_login(self.user)
        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)

        url = reverse("profile_page")
        self.assertEquals(resolve(url).func, profile_page)
        self.assertTemplateUsed(response, "profile.html")

    def test_user_logged_out_edit_account_redirect(self):
        """
        Test unauthorized users are redirected with a message
        when they try access the edit account page
        """

        response = self.client.get('/accounts/edit_account/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_edit_account(self):
        """
        Test edit account functionality works correctly for logged in users
        """

        self.client.force_login(self.user)
        response = self.client.get("/accounts/edit_account/1/")
        self.assertEqual(response.status_code, 200)

        url = reverse("edit_account", args=[self.user.id])
        self.assertEquals(resolve(url).func, edit_account)
        self.assertTemplateUsed(response, "edit_account.html")

        self.user.username = 'tony'
        form = {
            'username': 'tony',
            'first_name': 'tony',
            'last_name': 'gum',
            'email': 'test@example.com',
        }

        response = self.client.post('/accounts/edit_account/1/', form)

        self.assertEqual(self.user.username, 'tony')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Account updated successfully')
        self.assertEqual(response.status_code, 302)

    def test_user_logged_out_delete_account(self):
        """
        Test unauthorized users are redirected with a message
        when they try access the delete account page
        """

        response = self.client.get('/accounts/delete_account/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'You are not authorized to view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_user_logged_in_delete_account(self):
        """
        Test delete account functionality works correctly for logged in users
        """

        self.client.force_login(self.user)
        response = self.client.get("/accounts/delete_account/1/")
        self.assertEqual(response.status_code, 200)

        url = reverse("delete_account", args=[self.user.id])
        self.assertEquals(resolve(url).func, delete_account)
        self.assertTemplateUsed(response, "delete_account.html")

        response = self.client.post('/accounts/delete_account/1/')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Your account has been deleted')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.all().count(), 0)
