from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.models import *
# from bangazon_ui.models.orders_model import Orders

class TestOrderDetailView(TestCase):
        """
        A class to test the Order Detail View
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
            expiration_date="2017-01-01"
            )
        product = Product.objects.create(
            name="lego", 
            price=100, 
            description="ultimate lego set", 
            quantity=2, 
            customer_id=0, 
            product_type_id=0)

        Orders.objects.create(customer_id = 1, product_id = 2, completed=0, payment_type=1)

    def test_product_has_product(self):
        """
            a test method to check the order model field
        """

        prod = Orders.objects.get(product_id = 2)
        self.assertEqual(prod, 2)

        customer_id = Order.objects.get(customer_id=1)
        cust_id = Customer.objects.get(Customer[customer_id])

        self.assertIn(customer_id, cust_id)