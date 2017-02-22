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
        response = self.client.get(reverse('bangazon_ui:register'))
        self.assertEqual(response.status_code, 200)

        