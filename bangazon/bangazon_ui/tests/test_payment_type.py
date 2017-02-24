import sys
sys.path.append("../")
from django.test import TestCase
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.payment_type_model import Customer
from django.contrib.auth.models import User


class TestPaymentType(TestCase):
    """
    This is the test class for the PaymentType model
    Author: Dani Adkins
    """
    def setUp(self):

        user = User.objects.create_user(
            first_name="Dani",
            last_name="Dani",
            username="danidani",
            password="asdf1234"
            )

        customer = Customer.objects.create(
            user=user,
            address="3040 NSS Drive",
            city="Nashville",
            state="TN",
            zip_code="12345",
            phone="123456789"
            )

        payment = PaymentType.objects.create(
            customer=customer,
            payment_type="Visa",
            account_number="12345678",
            ccv="111",
            expiration_date="01/2017"
            )

    def test_payment_type_returns_defined_fields(self):
        """
        This test will test that the payment type information can be targeted and returned
        Author: Dani Adkins
        """
        payment = PaymentType.objects.get(payment_type="Visa")

        self.assertIsInstance(payment.customer, Customer)
        self.assertEqual(payment.payment_type, "Visa")
        self.assertEqual(payment.account_number, "12345678")
        self.assertEqual(payment.ccv,"111")
        self.assertEqual(payment.expiration_date, "01/2017")

    def test_payment_type_returns_posted_data(self):
        """
        This test will test that the payment type information will return the following information
        Author: Dani Adkins
        """
        payment_test = {
            'payment_type':'Visa',
            'account_number':'12345678',
            'ccv':'123',
            'expiration_date':'01/2017'
            }

        response = self.client.post(('bangazon_ui:payment_type_create'), payment_test)
        self.assertEqual(response.status_code, 404)
        # self.assertEqual(response.url, "/order")
        # assertContains("random string from order summary page that I know will be there")

