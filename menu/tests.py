from django.test import TestCase
from django.contrib.auth.models import User
from .models import MenuItem
from django.urls import reverse, resolve
from django.contrib.messages import get_messages
from .views import (
    menu_page,
    menu_drafts,
    add_menu_item,
    edit_menu_item,
    delete_menu_item,
)


class TestMenuViews(TestCase):
    """
    Tests the views for the menu app.
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

        menu_item = MenuItem.objects.create(
            title='Soup',
            )

        self.menu_item_form = {
            'title': 'Beef',
            'description': 'description',
            'available': True,
            'price': '10.00',
            'category': 'main',
            'status': '1'
        }

        self.menu_draft_form = {
            'title': 'Beef',
            'description': 'description',
            'available': True,
            'price': '10.00',
            'category': 'main',
            'status': 0
        }

    def test_menu_page_view(self):
        """
        Tests the menu page renders correctly
        """

        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)

        url = reverse('menu_page')
        self.assertEquals(resolve(url).func, menu_page)
        self.assertTemplateUsed(response, 'menu.html')

    def test_menu_drafts_view_for_staff(self):
        """
        Tests if the menu drafts page renders correctly
        for staff users
        """
        self.client.force_login(self.staff_user)
        response = self.client.get('/menu/drafts/')
        self.assertEqual(response.status_code, 200)

        url = reverse('menu_drafts')
        self.assertEquals(resolve(url).func, menu_drafts)
        self.assertTemplateUsed(response, 'menu_drafts.html')

    def test_menu_drafts_view_unauthorized_user_redirect(self):
        """
        Tests unauthorized users are redirected
        when they try access the menu drafts page
        """
        self.client.force_login(self.user)
        response = self.client.get('/menu/drafts/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Only logged in staff members can view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_staff_add_menu_item_page(self):
        """
        Tests add menu item page renders correctly for
        staff users
        """
        self.client.force_login(self.staff_user)
        response = self.client.get('/menu/add_menu_item/')
        self.assertEqual(response.status_code, 200)

        url = reverse('add_menu_item')
        self.assertEquals(resolve(url).func, add_menu_item)
        self.assertTemplateUsed(response, 'add_item.html')

    def test_unauthorized_users_add_item_redirect(self):
        """
        Tests if unauthorized users are redirected when they try
        to add a menu item
        """
        self.client.force_login(self.user)
        response = self.client.get('/menu/add_menu_item/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Only logged in staff members can view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_staff_can_add_menu_items(self):
        """
        Tests if staff can add new menu items
        """
        self.client.force_login(self.staff_user)
        response = self.client.post(
            '/menu/add_menu_item/',
            self.menu_item_form
            )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Menu item successfully published.'
                        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(MenuItem.objects.last().status, 1)
        self.assertEqual(MenuItem.objects.all().count(), 2)

    def test_staff_can_add_menu_drafts(self):
        """
        Tests if staff can add new menu drafts
        """
        self.client.force_login(self.staff_user)
        response = self.client.post(
            '/menu/add_menu_item/',
            self.menu_draft_form
            )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Menu draft saved as draft.'
                        )
        self.assertEqual(MenuItem.objects.last().status, 0)
        self.assertEqual(response.status_code, 302)

    def test_edit_menu_item_page_render_for_staff(self):
        """
        Tests if the menu edit page renders correctly
        for staff users
        """
        self.client.force_login(self.staff_user)

        response = self.client.get('/menu/edit_menu_item/1')
        self.assertEqual(response.status_code, 200)

        url = reverse('edit_menu_item', args=[1])
        self.assertEquals(resolve(url).func, edit_menu_item)
        self.assertTemplateUsed(response, 'add_item.html')

    def test_staff_can_edit_menu_items(self):
        """
        Tests if functionality for staff to edit menu items works
        for both editing as published and drafted
        """
        self.client.force_login(self.staff_user)

        response = self.client.post(
            '/menu/edit_menu_item/1',
            self.menu_draft_form
            )
        self.assertEqual(MenuItem.objects.last().status, 0)

        response = self.client.post(
            '/menu/edit_menu_item/1',
            self.menu_item_form
            )
        self.assertEqual(MenuItem.objects.last().status, 1)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Menu item saved as draft.'
                        )
        self.assertEqual(
                        str(messages[1]),
                        'Menu item has been edited and published.'
                        )

        self.assertEqual(response.status_code, 302)

    def test_edit_menu_item_unauthorised_user(self):
        """
        Tests if unauthorised users are redirected with
        a message if they try access the edit menu item page
        """
        self.client.force_login(self.user)
        response = self.client.get('/menu/edit_menu_item/1')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Only logged in staff members can view this page'
                        )
        self.assertEqual(response.status_code, 302)

    def test_delete_menu_item_page_render_for_staff(self):
        """
        Tests if the menu delete item page renders correctly
        for staff users
        """
        self.client.force_login(self.staff_user)

        response = self.client.get('/menu/delete_item/1/')
        self.assertEqual(response.status_code, 200)

        url = reverse('delete_item', args=[1])
        self.assertEquals(resolve(url).func, delete_menu_item)
        self.assertTemplateUsed(response, 'delete_item.html')

    def test_staff_can_delete_menu_items(self):
        """
        Tests if functionality for staff to delete
        menu items works
        """
        self.client.force_login(self.staff_user)

        response = self.client.post('/menu/delete_item/1/')

        self.assertEqual(MenuItem.objects.all().count(), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Menu item has been deleted.'
                        )

        self.assertEqual(response.status_code, 302)

    def test_delete_menu_item_unauthorised_user(self):
        """
        Tests if unauthorised users are redirected with
        a message if they try access the delete menu item page
        """
        self.client.force_login(self.user)
        response = self.client.get('/menu/delete_item/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
                        str(messages[0]),
                        'Only logged in staff members can view this page'
                        )
        self.assertEqual(response.status_code, 302)


class TestMenuModels(TestCase):
    """
    Tests the menu model
    """

    def setUp(self):

        self.menu_item = MenuItem.objects.create(
            title='Beef',
            )

    def test_default_values(self):
        """
        Tests that fields that have default values default
        to the correct value
        """

        self.assertEqual(self.menu_item.description, 'Menu item description')
        self.assertEqual(self.menu_item.available, True)
        self.assertEqual(self.menu_item.price, '00.00')
        self.assertEqual(self.menu_item.category, 'main')
        self.assertEqual(self.menu_item.status, 0)

    def test_model_returns_title_string(self):
        """
        Tests if the model returns the title of the
        menu item as a string
        """

        self.assertEquals(str(self.menu_item), 'Beef')
