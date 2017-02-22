import sys
sys.path.append("../")
from django.test import TestCase
from bangazon_ui.models.customer_model import Customer
from django.contrib.auth.models import User


class CustomerModelTest(TestCase):

    def test_customer_returns_object_with_defined_fields(self):
        """
        This test will test that the customer information can be targeted and returned
        Author: Dani Adkins
        """
        user = User.objects.create_user(first_name="Dani", last_name="Dani", username="danidani")
        customer = Customer.objects.create(user=user, address="3040 NSS Drive", city="Nashville", state="TN", zip_code="12345", phone="123456789")

        self.assertEqual(customer.user.first_name, "Dani")
        self.assertEqual(customer.user.last_name, "Dani")
        self.assertEqual(customer.user.username, "danidani")
        self.assertEqual(customer.address, "3040 NSS Drive")
        self.assertEqual(customer.city, "Nashville")
        self.assertEqual(customer.state, "TN")
        self.assertEqual(customer.zip_code, "12345")
        self.assertEqual(customer.phone, "123456789")
