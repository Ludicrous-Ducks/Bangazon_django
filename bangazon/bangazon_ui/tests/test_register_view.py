from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.views.register_view import Register
from django.contrib.auth.models import User
from django.urls import reverse
# from django.test import Client


class TestRegisterView(TestCase):
    """
    A Class to test the Register View
    """

    def test_register_view_should_post_correct_information(self):
        """
        The register view should return 200 if the post worked!
        """

        customer = {
            'first_name': "Dani",
            'last_name': "Dani",
            'username': "danidani",
            'email': 'd@d.com',
            'password': 'password',
            'address': "3040 NSS Drive",
            'city': "Nashville",
            'state': "TN",
            'zip_code': "12345",
            'phone': "123456789"
            }

        response = self.client.post(reverse('bangazon_ui:register'), customer)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login")

        